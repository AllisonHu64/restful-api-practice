from flask import Flask
from flask_restful import Api
from api.resources.users_api import UsersApi
from api.resources.user_api import UserApi
from api.config.config import Config


app = Flask(__name__)
api = Api(app)

api.add_resource(UsersApi, "{}users".format(Config.APPLICATION_ROOT))
api.add_resource(
    UserApi, 
    "{}user/<string:name>".format(Config.APPLICATION_ROOT),
    "{}user/<int:id>".format(Config.APPLICATION_ROOT), 
    "{}user".format(Config.APPLICATION_ROOT),
)
api.init_app(app)