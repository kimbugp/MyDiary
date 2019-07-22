"""Base module with test helper functions"""
import io
import json
import os
import unittest

from app.models.dbtasks import UserOperations
from app.utils import db
from app.utils.fixtures import create_tables
from config import app_config
from main import create_app


class TestingClass(unittest.TestCase):

    """Base Class for Testing the API"""

    def setUp(self):
        self.app = self.create_app()
        db.connect(self.app, auto_commit=True)
        self.database = UserOperations()
        create_tables()
        self.test_user = self.app.test_client()

    def tearDown(self):
        clear_user_table = "DELETE from users CASCADE"
        self.database.cursor.execute(clear_user_table)
        self.app_context.pop()

    def create_app(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app.testing = True
        self.client = self.app.test_client()
        self.request_context = self.app.test_request_context()
        self.url = '/api/v1'
        return self.app
