import unittest
from flask import Flask, jsonify, make_response, request
import sys
import json

from api import app
from api.v1.models import dbase
from api.v1.dbtasks import dboperations

database = dboperations()
db = dbase()
'''Dummy Data'''
test_user_data = {
    "username": "simon",
    "name": "Simon Peter",
    "email": "kimbugwe@gmail.com",
    "password": "12345678"
}


class all_entries_test(unittest.TestCase):

    def test_get_all_entries(self):
        test_user = app.test_client(self)
        response = test_user.get(
            "/api/v1/entries", content_type="application/json")
        self.assertEqual(response.status_code, 200)


class user_tests(unittest.TestCase):

    # def setUp(self):
        # db.conn('postgres://postgres:postgres@localhost:5432/diarydb_test')

    def test_user_signup(self):
        test_user = app.test_client(self)
        response = test_user.post(
            "/api/v1/auth/signup", data=json.dumps(test_user_data), content_type="application/json")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
