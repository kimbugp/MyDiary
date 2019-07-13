"""Base module with test helper functions"""
import io
import json
import os
import unittest
from app.models.dbtasks import UserOperations
from app.utils.fixtures import create_tables
from config import app_config

from app import app, db

database = UserOperations()


class TestingClass(unittest.TestCase):

    """Base Class for Testing the API"""

    def setUp(self):
        self.app = app
        self.app.config.from_object(app_config.get('testing'))
        self.app.testing = True
        # change test db
        db_url = app.config.get('TEST_DATABASE_URL')
        db.get_connection(db_url, auto_commit=True)
        create_tables()
        self.test_user = self.app.test_client()

    def tearDown(self):
        clear_user_table = "DELETE from users CASCADE"
        database.cursor.execute(clear_user_table)
