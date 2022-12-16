class Config(object):
    APPLICATION_ROOT = '/ztgg-backend-api/v1/'
    MONGO_PORT = 30001
    MONGO_DB_NAME = "ztgg_demo_db"
    ZTGG_DOMAIN = "localhost"
    MONGO_URL = 'mongodb://{}:{}/'.format(ZTGG_DOMAIN, MONGO_PORT)
    DEFAULT_CREATOR = "App_Admin"