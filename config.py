"""Module to configure database"""
db_user = 'postgres'
user_password = 'qwertyuiop'


class Config:
    """Class to configure database"""
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    """Class to configure database to developer"""
    db_name = 'diarydb'
    # DEBUG = True
    # # TESTING = False
    DATABASE_URL = 'postgresql://' + db_user + ': ' + \
        user_password + '@localhost/' + db_name + ''


class TestingConfig(Config):
    """Class to configure database to testing"""
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
