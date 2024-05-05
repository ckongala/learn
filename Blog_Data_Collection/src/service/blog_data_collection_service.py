from fastapi import HTTPException
from googleapiclient.discovery import build
import requests
import json
from src.service.logger_config import get_application_logger
from src.service.mongo_service import mongo_service
from src.models.model import Blog, Status, MONGO_LOCAL_CONNECTION_STRING
from src.service.data_object_converter import DataObjectConverter

class BlogDataService:
    def __init__(self):
        self.logger = get_application_logger()
        self.mongo_service = mongo_service(MONGO_LOCAL_CONNECTION_STRING)
        self.post_collection = self.mongo_service.get_mongo_collection(
            database_name=Blog.BLOG_DATABASE.value,
            collection_name=Blog.BLOG_METADATA_COLLECTION.value
        )
        pass

    def url_extraction(self, search_term, DEVELOPER_KEY, CX_ID, start, DIFF_BOT_TOKEN, task_id):
        extracted_urls = []
        search_terms_list = search_term
        self.logger.info(f"Blog Database {Blog.BLOG_DATABASE.value}")
        self.mongo_service.update_task_status(task_id=task_id, new_status=Status.running.value, database_name=Blog.BLOG_DATABASE.value, collection_name=Blog.BLOG_METADATA_COLLECTION.value)

        try:
            service = build("customsearch", "v1", developerKey=DEVELOPER_KEY)
            for keyword in search_terms_list:
                lis = []
                for _ in range(1, 2):  # Adjust range as needed
                    res = service.cse().list(q=keyword, cx=CX_ID, start=start).execute()
                    if 'items' in res:
                        for result in res['items']:
                            lis.append(result['link'])
                    start += 3  # Assuming 3 results per page; adjust as needed
                extracted_urls.append({keyword:lis})

            self.logger.info(f"link are here {extracted_urls}")
            self.mongo_service.update_task_status(task_id=task_id, new_status=Status.phase_1.value, extracted_urls=extracted_urls, database_name=Blog.BLOG_DATABASE.value, collection_name=Blog.BLOG_METADATA_COLLECTION.value)

            self.mongo_service.update_task_status(task_id=task_id, new_status=Status.phase_2.value, extracted_urls=extracted_urls, database_name=Blog.BLOG_DATABASE.value, collection_name=Blog.BLOG_METADATA_COLLECTION.value)
            for key_dict in extracted_urls:
                for _, urls in key_dict.items():
                    for url in urls:
                        i = 0
                        self.logger.info(f"urls {url}")
                        if not any(excluded_site in url for excluded_site in ['wikipedia', 'facebook', 'youtube']):
                            api_url = f"https://api.diffbot.com/v3/article?token={DIFF_BOT_TOKEN}&url={url}&maxToCrawl=1&maxToProcess=1"
                            response = requests.get(api_url)
                            data = json.loads(response.text)
                            if "objects" in data and len(data['objects']) > 0:
                                config = {
                                         'order': ["type", "text", "tags", "siteName", "publisherRegion", "publisherCountry", "pageUrl", "images", "icon", "humanLanguage", "estimatedDate", "diffbotUri", "date", "categories", "authors", "authorUrl", "author", "sentiment"], 
                                         'native_fields': ["type", "text", "tags", "siteName", "publisherRegion", "publisherCountry", "pageUrl", "images", "icon", "humanLanguage", "estimatedDate", "diffbotUri", "date", "categories", "authors", "authorUrl", "author"],
                                         'computed_fields': ["sentiment"], 
                                         'media_id': data["objects"][0]["pageUrl"], 
                                         'media_type': 'blog', 
                                         'media_sub_type': 'post' 
                                         }
                                self.mongo_service.update_task_status(task_id=task_id, new_status=Status.phase_3.value, extracted_urls=extracted_urls, database_name=Blog.BLOG_DATABASE.value, collection_name=Blog.BLOG_METADATA_COLLECTION.value)
                                data_object_converter = DataObjectConverter(config=config)
                                formatted_data = data_object_converter.convert_to_desired_format(data=data["objects"][0]) 
                                self.mongo_service.load_to_mongo(data=formatted_data, database_name=Blog.BLOG_DATABASE.value, collection_name=Blog.BLOG_DATA_COLLECTION.value)
                                i+=1
                                self.logger.info(f"Data insertion process completed for {i} record")
                            else:
                                self.logger(f"There is no blog data for this url: {url}")
                                pass

            self.mongo_service.update_task_status(task_id=task_id, new_status=Status.completed.value, database_name=Blog.BLOG_DATABASE.value, collection_name=Blog.BLOG_METADATA_COLLECTION.value)

            return extracted_urls

        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))