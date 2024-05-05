from bson import ObjectId
from fastapi import APIRouter, FastAPI, HTTPException, BackgroundTasks
from os.path import abspath, join, dirname
import os
import random
import string
from dotenv import load_dotenv
from src.service.logger_config import get_application_logger
from src.models.model import BlogDataRequest, Blog, MONGO_LOCAL_CONNECTION_STRING
from src.service.mongo_service import mongo_service
from src.service.blog_data_collection_service import BlogDataService

class BlogDataCollector:
    def __init__(self):
        env_path = abspath(join(dirname(__file__), "../..", '.env'))
        load_dotenv(env_path, verbose=True)

        self.mongo_service = mongo_service(MONGO_LOCAL_CONNECTION_STRING)
        self.post_collection = self.mongo_service.get_mongo_collection(
            database_name=Blog.BLOG_DATABASE.value,
            collection_name=Blog.BLOG_METADATA_COLLECTION.value
        )
        self.blog_data_service = BlogDataService()
        self.developer_key = os.getenv("GOOGLE_DEVELOPER_KEY")
        self.cx_id = os.getenv("GOOGLE_CX_ID")
        self.diff_bot_token = os.getenv("DIFF_BOT_TOKEN")
        self.logger = get_application_logger()
        self.task_id= ''.join(random.choices(string.digits + string.ascii_letters, k=7))

    def collect_blog_data(self, request: BlogDataRequest):
        self.logger.info("Received a blog data collection request.")
        if not all([self.developer_key, self.cx_id, self.diff_bot_token]):
            raise HTTPException(status_code=500, detail="Server is not properly configured with Google API keys.")
        
        data = {"task_id": self.task_id, "search_term": request.search_term, "message": request.message, "status": "Started"}

        existing_data = self.post_collection.find_one({"task_id": self.task_id})
        if existing_data is None:
            self.post_collection.insert_one(data)
            data['_id'] = str(data['_id'])
            self.logger.info(f"Inserted data: {data}")
        else:
            existing_data['_id'] = str(existing_data['_id']) 
            data = existing_data
            self.logger.info(f"Data already exists: {existing_data}")
        self.logger.info("Data insertion process completed.")

        return {"data": data}
    
    def background_url_extraction(self, search_term, developer_key, cx_id, start, diff_bot_token, task_id):
        blog_data = self.blog_data_service.url_extraction(
            search_term=search_term, 
            DEVELOPER_KEY=developer_key, 
            CX_ID=cx_id,
            start=start, 
            DIFF_BOT_TOKEN=diff_bot_token, 
            task_id=task_id
            )
        self.logger.info(f"Background Blog data extraction completed with links: {blog_data}")

app = FastAPI(json_encoders={ObjectId: lambda oid: str(oid)})
router = APIRouter()

blog_data_collector = BlogDataCollector()  

@router.post("/api/v1/blog/task")
async def blog_data_collection_endpoint(request: BlogDataRequest, background_tasks: BackgroundTasks):
    """
    Endpoint for collecting blog data.
    """
    data = blog_data_collector.collect_blog_data(request)

    background_tasks.add_task(
        blog_data_collector.background_url_extraction,
        search_term=request.search_term,
        developer_key=blog_data_collector.developer_key,
        cx_id=blog_data_collector.cx_id,
        diff_bot_token=blog_data_collector.diff_bot_token, 
        task_id=blog_data_collector.task_id,
        start=request.start
    )
    return data 
