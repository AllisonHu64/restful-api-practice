"""Contains a handler for MongoDB database.

Encapsulates some commonly used MongoDB functionality.
"""

from pymongo import MongoClient, ReturnDocument
from api.config.config import Config

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
        db_name = Config().MONGO_DB_NAME
        db_url = Config().MONGO_URL
        client = MongoClient(db_url)
        self._db = client[db_name]

    
    def insert_one(self, col, document):
        return self._db[col].insert_one(document)

    def find(self, col, filter=None):
        return self._db[col].find(filter)
    
    def find_one(self, col, filter=None):
        return self._db[col].find_one(filter)

    def find_one_with_sort(self, col, filter=None, sort=None):
        return self._db[col].find_one(filter, sort=sort)

    def update_one(self, col, filter, update):
        return self._db[col].update_one(filter, update)
    
    def delete_one(self, col, filter=None):
        return self._db[col].delete_one(filter)
        
    def count_documents(self, col, filter=None):
        return self._db[col].count_documents(filter)
