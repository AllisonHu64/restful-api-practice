""" Adds api resources to Flask application.
"""
from api.config.config import Config
from api.resources.user_api import UserApi
from api.resources.users_api import UsersApi
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(UsersApi, "{}users".format(Config.instance().APPLICATION_ROOT))
api.add_resource(
    UserApi, 
    "{}user/<string:name>".format(Config.instance().APPLICATION_ROOT),
    "{}user/<int:id>".format(Config.instance().APPLICATION_ROOT), 
    "{}user".format(Config.instance().APPLICATION_ROOT),
)
api.init_app(app)