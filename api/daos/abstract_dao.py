"""Contains an abstract data access object class.

Encapsulates some commonly used functionality of a data object.
"""
from api.config.config import Config
from api.errors.errors import IdNotExistInCollection
from api.utils.utils import current_milli_time
import pymongo

class AbstractDao():
    """Handles common operations for an data access object with a unique ID.
    for example: insert_one, find_one_with_id, modify_one_with_id and 
    delete_with_id.

    Attributes:
        _db: A database client.
        _schema: A Schema for the data object.
        _col: A database/collection name of the data object.
    """
    def __init__(self, schema, col, db_client):
        self._db = db_client
        self._schema = schema
        self._col = col
    
    def delete_one_by_id(self, id):
        assert isinstance(id, int)
        if self._db.count_documents(self._col, {'id': id}) == 0:
            raise IdNotExistInCollection
        return self._db.delete_one(self._col, {'id': id})

    def find_all(self):
        return self._schema.dump(self._db.find(col=self._col), many=True)
    
    def find_one_by_id(self, id):
        assert isinstance(id, int)
        return self._schema.dump(self._db.find_one(self._col, filter={"id":id}))
    
    def get_new_id(self):
        userWithMaxId = self._db.find_one_with_sort(self._col, sort=[("id", pymongo.DESCENDING)])
        if userWithMaxId == None:
            return 1
        else:
            return userWithMaxId["id"] + 1

    def insert_one(self, document):
        assert isinstance(document, dict)
        document["id"] = self.get_new_id()
        now = current_milli_time()

        document["updatedInMS"] = now
        if "updatedBy" not in document:
            document["updatedBy"] = Config.instance().DEFAULT_CREATOR
        
        document["createdInMS"] = now
        if "createdBy" not in document:
            document["createdBy"] = Config.instance().DEFAULT_CREATOR
        return self._db.insert_one(self._col, document)
    
    def update_one_by_id(self, id, document):
        assert isinstance(id, int)
        assert isinstance(document, dict)
        if self._db.count_documents(self._col, {'id': id}) == 0:
            raise IdNotExistInCollection

        document["updatedInMS"] = current_milli_time()
        if "updatedBy" not in document:
            document["updatedBy"] = Config.instance().DEFAULT_UPDATOR
        
        selector = {"id": id}
        update = {"$set": document}
        return self._db.update_one(self._col, selector, update)