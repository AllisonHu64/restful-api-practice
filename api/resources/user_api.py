from api.config.config import Config
from api.daos.user_dao import UserDao
from api.errors.errors import IdNotExistInCollection
from api.utils.utils import verify_contain_all_fields, verify_contain_some_fields
from flask_restful import Resource
from flask import request, json
from http import HTTPStatus

class UserApi(Resource):
    def __init__(self):
        self._dao = UserDao()
        super().__init__()
    def get(self, name=None):
        if name == None:
            message = "Name can't be empty. GET {}user/:name".format(Config().APPLICATION_ROOT)
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        res = self._dao.find_one_by_name(name)
        if len(res.keys()) == 0:
            message = "User with name [{}] doesn't exist".format(name)
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        return res, HTTPStatus.OK
    def post(self):
        user = request.get_json()
        required_fields = ["name", "age"]
        if not verify_contain_all_fields(user, required_fields):
            message = "Please provide {} fields in payload".format(required_fields)
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        
        if not self._dao.is_name_unique(user["name"]):
            message = "Name [{}] is not unique".format(user["name"])
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        
        self._dao.insert_one(user)
        return {"status": HTTPStatus.OK, "message": "Sucessfully inserted"}, HTTPStatus.OK

    def patch(self):
        user = request.get_json()
        required_fields = ["id"]
        if not verify_contain_all_fields(user, required_fields):
            message = "Please provide {} fields in payload".format(required_fields)
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        
        optional_fields = ["name", "age"]
        if not verify_contain_some_fields(user, optional_fields):
            message = "Please provide at least one of {} fields in payload".format(required_fields)
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST

        if "name" in user:
            similar_user = self._dao.find_one_by_name(user["name"])
            if "id" in similar_user and similar_user["id"] != user["id"]:
                print("jaajjaja")
                message = "Name [{}] is not unique".format(user["name"])
                return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        
        id = user["id"]
        user.pop("id")
        try:
            self._dao.update_one_by_id(id, user)
        except IdNotExistInCollection:
            message = "Id [{}] doesn't exist in collection".format(id)
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        return {"status": HTTPStatus.OK, "message": "Sucessfully updated"}, HTTPStatus.OK
    
    def delete(self, id=None):
        if id == None:
            message = "Id can't be empty. DELETE {}user/:id".format(Config().APPLICATION_ROOT)
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        try:
            self._dao.delete_one_by_id(id)
        except IdNotExistInCollection:
            message = "Id [{}] doesn't exist in collection".format(id)
            return {"status": HTTPStatus.BAD_REQUEST, "message": message}, HTTPStatus.BAD_REQUEST
        return {"status": HTTPStatus.OK, "message": "Sucessfully deleted"}, HTTPStatus.OK
    