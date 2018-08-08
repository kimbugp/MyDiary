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
    DATABASE_URL = 'postgresql://' + db_user + ': ' + \
        user_password + '@localhost/' + db_name + \
        '' or "postgres://zjmricklwnsavr:1842468d\
        23fa9a32e29cccbec9163b97cd4480ef\
        949084cc7524fdf9cccc4a20@ec2-54-221-210-97.compute-1.amazonaws.com:\
        5432/dcqilp2it5cbhp"


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
