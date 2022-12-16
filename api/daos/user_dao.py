from api.daos.abstract_dao import AbstractDao
from api.schema.user_schema import UserSchema
from api.database.mongo import MongoDBHandler

class UserDao(AbstractDao):
    def __init__(self):
        super().__init__(UserSchema(), "user" , MongoDBHandler())
    def is_name_unique(self, name):
        assert isinstance(name, str)
        return self._db.count_documents(self._col, filter={"name":name}) == 0
    def find_one_by_name(self, name):
        assert isinstance(name, str)
        return self._schema.dump(self._db.find_one(self._col, filter={"name":name}))