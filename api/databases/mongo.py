"""Contains a handler for MongoDB database.
Encapsulates some commonly used MongoDB functionality.
"""
from api.config.config import Config
from pymongo import MongoClient, ReturnDocument
import logging

class MongoDBHandler():
    """Handles common Mongo Database operations, such as insert,
    find, modify and delete.
    Attributes:
        _db: A mongo client.
        _logger: A logger.
    """

    def __init__(self):
        """Inits MongoDBHandlerClass with app.
        Args:
            app: An application that contains a config.MONGO_HOST 
            attribute.
        """
        db_name = Config.instance().MONGO_DB_NAME
        db_url = Config.instance().MONGO_URL
        client = MongoClient(db_url)
        self._db = client[db_name]
        self._logger = logging.getLogger(__name__)
        self._logger.info("Subbcessfully initialized MongoDB Handler with {}".format(db_url))
    
    def count_documents(self, col, filter=None):
        return self._db[col].count_documents(filter)

    def delete_one(self, col, filter=None):
        return self._db[col].delete_one(filter)

    def find(self, col, filter=None):
        return self._db[col].find(filter)
    
    def find_one(self, col, filter=None):
        return self._db[col].find_one(filter)

    def find_one_with_sort(self, col, filter=None, sort=None):
        return self._db[col].find_one(filter, sort=sort)

    def insert_one(self, col, document):
        return self._db[col].insert_one(document)

    def update_one(self, col, filter, update):
        return self._db[col].update_one(filter, update)