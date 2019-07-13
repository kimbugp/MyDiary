"""Model for database"""
import os

import psycopg2
from psycopg2.extras import RealDictCursor


class DATABASE():
    """Class  for database"""

    def __init__(self, app=None):
        self.app = app

    @classmethod
    def connect(cls, app, connector=psycopg2, auto_commit=False):
        database = app.config.get('DATABASE_URL')
        cls.get_connection(database, connector, auto_commit)
        return cls(app)

    @classmethod
    def get_connection(cls, database, connector=psycopg2, auto_commit=False):
        cls.conn = connector.connect(database)
        cls.conn.autocommit = auto_commit
        return cls.conn

    def create_user_table(self):
        """Method to create user table"""
        user_table = ("CREATE TABLE IF NOT EXISTS users"
                      "(user_id serial  NOT NULL PRIMARY KEY,"
                      "username VARCHAR(50) UNIQUE NOT NULL,"
                      "name VARCHAR(50) NOT NULL,"
                      "profession VARCHAR(50),"
                      "profilepic VARCHAR(300),"
                      "email VARCHAR(80) UNIQUE NOT NULL,"
                      "password VARCHAR(200) NOT NULL)")
        self.cursor.execute(user_table)

    def create_entries_table(self):
        """Method to create entries table"""
        entries_table = ("CREATE TABLE IF NOT EXISTS entries"
                         "(entry_id serial  NOT NULL PRIMARY KEY,"
                         "entry_date TIMESTAMP NOT NULL,"
                         "entry_name VARCHAR(50) NOT NULL,"
                         "entry_content text NOT NULL,"
                         "user_id INTEGER,FOREIGN KEY (user_id)\
                          REFERENCES users(user_id) ON DELETE CASCADE)")

        self.cursor.execute(entries_table)

    @property
    def cursor(self):
        return self.conn.cursor()

    @property
    def dict_cursor(self):
        return self.conn.cursor(
            cursor_factory=RealDictCursor)
