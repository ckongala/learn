from fastapi import FastAPI
from googleapiclient.discovery import build
from src.service.logger_config import get_application_logger
from src.controllers.ping_controller import router as ping_router
from src.controllers.blog_data_controller import router as blog_router
from src.controllers.get_blog_data_controller import router as get_blog_data
from src.controllers.monitor_diffbot_controller import router as monitor_router

app = FastAPI()
logger = get_application_logger()

app.include_router(ping_router)
app.include_router(blog_router)
app.include_router(get_blog_data)
app.include_router(monitor_router)