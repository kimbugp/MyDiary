"""Model for database"""
import psycopg2
from psycopg2.extras import RealDictCursor
from config import DevelopmentConfig,TestingConfig


class dbase():
    """Class  for database"""
    def __init__(self):
        try:
            self.conn = psycopg2.connect(DevelopmentConfig.DATABASE_URL)
            self.cursor = self.conn.cursor()
            self.dict_cursor = self.conn.cursor(
                cursor_factory=RealDictCursor)
            self.conn.autocommit = True
        except psycopg2.DatabaseError as error:
            print(error)

    def create_user_table(self):
        """Method to create user table"""
        user_table = ("CREATE TABLE IF NOT EXISTS users"
                      "(user_id serial  NOT NULL PRIMARY KEY,"
                      "username VARCHAR(50) UNIQUE NOT NULL,"
                      "name VARCHAR(50) NOT NULL,"
                      "email VARCHAR(80) UNIQUE NOT NULL,"
                      "password VARCHAR(200) NOT NULL)")
        self.cursor.execute(user_table)

    def create_entries_table(self):
        """Method to create entries table"""
        entries_table = ("CREATE TABLE IF NOT EXISTS entries"
                         "(entry_id serial  NOT NULL PRIMARY KEY,"
                         "entry_date TIMESTAMP NOT NULL,"
                         "entry_name VARCHAR(50) NOT NULL,"
                         "entry_content VARCHAR(80) NOT NULL,"
                         "user_id INTEGER ,FOREIGN KEY (user_id)\
                          REFERENCES users(user_id) ON DELETE CASCADE)")

        self.cursor.execute(entries_table)
