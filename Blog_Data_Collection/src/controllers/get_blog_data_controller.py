from fastapi import FastAPI, HTTPException
from bson import ObjectId
from fastapi import APIRouter
from src.service.logger_config import get_application_logger
from src.service.mongo_service import mongo_service
from src.models.model import Blog, MONGO_LOCAL_CONNECTION_STRING

router = APIRouter()
app = FastAPI()

class BlogDataAPI:
    def __init__(self, connection_string):
        self.mongo_service = mongo_service(connection_string)
        self.post_collection = self.mongo_service.get_mongo_collection(
            database_name=Blog.BLOG_DATABASE.value,
            collection_name=Blog.BLOG_METADATA_COLLECTION.value
        )
        self.logger = get_application_logger()


blog_data_api = BlogDataAPI(MONGO_LOCAL_CONNECTION_STRING)

def convert_objectid_to_string(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
            elif isinstance(value, dict):
                convert_objectid_to_string(value)
    elif isinstance(data, list):
        for item in data:
            convert_objectid_to_string(item)
    return data


@router.get("/api/v1/task/{task_id}")
async def get_blog_data_status(task_id: str):
    filter_query = {"task_id": str(task_id)}
    data = blog_data_api.post_collection.find_one(filter_query)
    if data is None:
        raise HTTPException(status_code=404, detail="No blog data found for this task ID")
    return data

