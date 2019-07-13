from os import environ


class BaseConfig(object):
    DEBUG = True
    DATABASE_URL = environ.get("DATABASE_URL")
    SECRET_KEY = environ.get("SECRET_KEY")


class Development(BaseConfig):
    pass


class Staging(BaseConfig):
    DEBUG = False


class Production(Staging):
    pass


class Testing(BaseConfig):
    TESTING = True
    TEST_DATABASE_URL = environ.get("TEST_DATABASE_URL")


app_config = {
    'development': Development,
    'staging': Staging,
    'production': Production,
    'testing': Testing
}
