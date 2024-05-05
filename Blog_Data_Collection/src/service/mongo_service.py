from pymongo import MongoClient
from pymongo import errors
from src.service.logger_config import get_application_logger

logger = get_application_logger()


class mongo_service:

    def __init__(self, connection_str):
        try:
            self.mongo_connection = MongoClient(connection_str, serverSelectionTimeoutMS=5000)
            logger.info('Mongo connection established to %s', connection_str)
        except errors.Any as error:
            logger.error('Failed to connect to MongoDB: ', error)

    def get_connection(self):
        """
        Getting the connection with MongoDB.
        """
        return self.mongo_connection

    def get_mongo_collection(self, database_name, collection_name):
        """
        Taking arguments as Database name and Collection name,
        Checking the connection and Handling the error exception.
        Returning the table
        """

        collection = None
        try:
            db = self.mongo_connection[database_name]
            collection = db[collection_name]
        except errors.Any as error:
            logger.error('Failed to get mongo table: ', error)
        return collection

    def load_to_mongo(self, data, database_name: str, collection_name: str):
        mongo_table = self.get_mongo_collection(
            database_name,
            collection_name)
        if len(data) > 0:
            inserted_documents_count = len(mongo_table.insert_many(data).inserted_ids)
            logger.info(self.get_insert_log(database_name, collection_name, inserted_documents_count))
        else:
            logger.info('No posts to load to mongo')
        return

    def close_connection(self):
        """
        Closing the connection with MongoDB.
        """
        self.mongo_connection.close()

    def get_insert_log(self, database_name: str, collection_name: str, inserted_documents_count: int):
        return 'Inserted ' + str(inserted_documents_count) + ' documents into ' + database_name + '.' + collection_name
    
    def update_task_status(self, task_id, new_status, database_name, collection_name, extracted_urls=None):
        """
        Updates the status of a task identified by Task_id and optionally adds extracted URLs(DATA).
        """
        collection = self.get_mongo_collection(database_name, collection_name)
        if collection is not None:
            update_data = {"status": new_status}
            if extracted_urls is not None:
                update_data["extracted_URLs"] = extracted_urls
            result = collection.update_one(
                {"task_id": task_id},
                {"$set": update_data}
            )
            if result.modified_count > 0:
                logger.info(f"Updated status to {new_status} for Task_id {task_id}.")
            else:
                logger.info(f"No document found with Task_id {task_id} to update.")
            return result
        else:
            logger.error("Failed to retrieve the collection for updating.")
