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
    DATABASE_URL = "postgres://ezymjdsrogukfj:394336d320362\
        66cd504ec43d602407c04d5a81a83e3f5973dc5f12bae5c55\
        5c@ec2-54-243-61-173.compute-1.amazonaws.com:5432/\
        d5uu5bi14khue"
        # 'postgresql://' + db_user + ': ' + \
        # user_password + '@localhost/' + db_name + \
        # '' or 


class TestingConfig(Config):
    """Class to configure database to testing"""
    db_name = 'diarydb_test'
    TESTING = True
    DATABASE_URL = 'postgresql://' + db_user + ': ' + \
        user_password + '@localhost/' + db_name + ''


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
