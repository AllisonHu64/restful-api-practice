from flask_restful import Resource
from api.database.mongo import MongoDBHandler
from api.daos.user_dao import UserDao
from api.schema.user_schema import UserSchema

class UsersApi(Resource):
    def __init__(self):
        self._dao = UserDao()
        super().__init__()
    def get(self):
        return self._dao.find_all()
        