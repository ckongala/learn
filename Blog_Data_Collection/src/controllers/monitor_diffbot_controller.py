from fastapi import APIRouter, HTTPException
from src.service.logger_config import get_application_logger
import requests
import datetime
from dateutil.relativedelta import relativedelta
from os.path import abspath, join, dirname
from dotenv import load_dotenv
import os

# Load environment variables
env_path = abspath(join(dirname(__file__), "../..", '.env'))
load_dotenv(env_path, verbose=True)
logger = get_application_logger()


router = APIRouter()

class BillingCycle:
    """Handles billing cycle calculations."""
    def __init__(self, day_renews=8):
        self.day_renews = day_renews

    def calculate_days(self, dnow=None):
        """Calculate days in the current billing cycle."""
        try:
            dnow = dnow or datetime.datetime.now()
            if dnow.day >= self.day_renews:
                drenew = datetime.datetime(dnow.year, dnow.month, self.day_renews)
            else:
                drenew = datetime.datetime(dnow.year, dnow.month - 1, self.day_renews)

            delta = dnow - drenew
            return delta.days + 1
        except Exception as e:
            logger.error(f"Request failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))


class DiffBotAPI:
    """Handles API interactions with DiffBot."""
    def __init__(self, token):
        self.token = token

    def get_account_usage(self, days):
        """Get account usage from the DiffBot API."""
        try:
            response = requests.get(f"https://api.diffbot.com/v4/account?token={self.token}&days={days}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Request failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    def process_usage(self, api_response):
        """Process usage details and calculate the percentage used."""
        try:
            total_usage = sum([x['credits'] for x in api_response['usage']])
            percentage = (total_usage/api_response["planCredits"])*100 if "planCredits" in api_response else 0
            planCredits = api_response["planCredits"] if "planCredits" in api_response else total_usage +1
            return total_usage, percentage, planCredits
        except Exception as e:
            logger.error(f"Request failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))


# Initialize components
diff_bot_token = os.getenv("DIFF_BOT_TOKEN")
if not diff_bot_token:
    raise ValueError("DIFF_BOT_TOKEN is not set in environment Variables")
billing_cycle = BillingCycle()
diff_api = DiffBotAPI(diff_bot_token)


@router.get("/api/v1/diffbot/monitor")
async def diff_check_account_balance():
    """Endpoint to check and report the usage of Diffbot API credits."""
    try:
        days = billing_cycle.calculate_days()
        api_response = diff_api.get_account_usage(days)
        total_usage, percentage, planCredits = diff_api.process_usage(api_response)

        if total_usage >= planCredits:
            error_message = f"You have exceeded the API limit for this key!! Over the last 30 days you have used {total_usage} credits. Stop Now!!!"
            logger.error(error_message)
            raise HTTPException(status_code=400, detail=error_message)

        if int(percentage) in range(50, 100):
            logger.info(f"Current Diffbot credit usage: {int(percentage)}%")

        return {"total_usage": total_usage, "percentage": int(percentage)}
    except requests.RequestException as req_error:
        logger.error(f"Request failed: {req_error}")
        raise HTTPException(status_code=500, detail=str(req_error))
    except Exception as e:
        logger.error(f"Request failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

