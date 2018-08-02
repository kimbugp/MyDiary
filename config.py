import os
db_user = 'postgres'
user_password = 'qwertyuiop'


class Config:
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    db_name = 'diarydb'
    # DEBUG = True
    # # TESTING = False
    DATABASE_URL = 'postgresql://' + db_user + ': ' + \
        user_password + '@localhost/' + db_name + ''


class TestingConfig(Config):
    db_name = 'diarydb_test'
    # DEBUG = True
    TESTING = True
    DATABASE_URL = 'postgresql://' + db_user + ': ' + \
        user_password + '@localhost/' + db_name + ''


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}

# def configure_app(configuration):
#     app.config.from_object(configuration)