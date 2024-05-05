from typing import Optional
from pydantic import BaseModel
from enum import Enum

MONGO_LOCAL_CONNECTION_STRING='mongodb://localhost:27017/'


class BlogDataRequest(BaseModel):
    search_term: list
    message: str 
    start: Optional[int] = 1


class Status(Enum):
    running = "Running, URLs collection in progress"
    phase_1 = "URLs collection completed"
    phase_2 = "Started Data collection"
    phase_3 = "Data collection in process"
    completed = "Blog data collection Completed"

class Blog(Enum):
    BLOG_DATABASE = "blogs"
    BLOG_METADATA_COLLECTION = "metadata"
    BLOG_DATA_COLLECTION = "records"