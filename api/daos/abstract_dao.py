import pymongo
from api.utils.utils import current_milli_time
from api.config.config import Config
from api.errors.errors import DuplicateIdInCollection, IdNotExistInCollection

class AbstractDao():
    def __init__(self, schema, col, db_client):
        self._db = db_client
        self._schema = schema
        self._col = col


    def insert_one(self, document):
        assert isinstance(document, dict)
        document["id"] = self.get_new_id()
        now = current_milli_time()

        document["updatedInMS"] = now
        if "updatedBy" not in document:
            document["updatedBy"] = Config().DEFAULT_CREATOR
        
        document["createdInMS"] = now
        if "createdBy" not in document:
            document["createdBy"] = Config().DEFAULT_CREATOR
        return self._db.insert_one(self._col, document)
    
    def delete_one_by_id(self, id):
        assert isinstance(id, int)
        if self._db.count_documents(self._col, {'id': id}) == 0:
            raise IdNotExistInCollection
        return self._db.delete_one(self._col, {'id': id})
    
    def update_one_by_id(self, id, document):
        assert isinstance(id, int)
        assert isinstance(document, dict)
        if self._db.count_documents(self._col, {'id': id}) == 0:
            raise IdNotExistInCollection

        document["updatedInMS"] = current_milli_time()
        if "updatedBy" not in document:
            document["updatedBy"] = Config().DEFAULT_CREATOR
        
        selector = {"id": id}
        update = {"$set": document}
        return self._db.update_one(self._col, selector, update)
    
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


        
        

