import os

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.
    """

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned. 
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class Config:
    """Configuration information for database and flask.

    Attributes:
        APPLICATION_ROOT: Base route url for backend api.
        MONGO_DB_NAME: Mongo database name.
        DEFAULT_CREATOR: Default creator of documents in collections.
        DEFAULT_UPDATOR: Default updator of documents in collections.
        MONGO_DOMAIN: Domain of Mongo database application.
        MONGO_PORT: Port of Mongo database application.
        MONGO_URL: Url of Mongo databse application.
    """
    APPLICATION_ROOT = '/rest-practice-backend/v1/'
    MONGO_DB_NAME = 'rest_practice_db'
    DEFAULT_CREATOR = 'App_Admin'
    DEFAULT_UPDATOR = 'App_Admin'

    def __init__(self):
        # TODO(AllisonHu64) add config for development environment and production environment
        run_env = os.environ.get('RUN_ENV') or 'local'
        if run_env == 'local':
            self.MONGO_DOMAIN = 'localhost'
            self.MONGO_PORT = 30001
        elif run_env == 'development':
            self.MONGO_DOMAIN = os.environ.get('MONGO_DOMAIN')
            self.MONGO_PORT = os.environ.get('MONGO_PORT')
        self.MONGO_URL = 'mongodb://{}:{}/'.format(self.MONGO_DOMAIN, self.MONGO_PORT)

