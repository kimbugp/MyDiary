import unittest
from flask import Flask, jsonify, make_response, request
import sys
import json

from api import app
from api.v1.models import dbase
from api.v1.dbtasks import dboperations

database = dboperations()
db = dbase()
cursor = db.cursor

test_user_data = {
    "username": "peter",
    "name": "Simon Peter",
    "email": "kimbugwe@gmail.com",
    "password": "12345678"
}
test_sign_in = {
    "username": "peter",
    "password": "12345678"
}
test_entry = {
    "entry_name": "Test name",
    "entry_content": "Test content"
}


class all_entries_test(unittest.TestCase):

    def setUp(self):
        test_user = app.test_client(self)
        test_user.post(
            "/api/v1/auth/signup", data=json.dumps(test_user_data), content_type="application/json")
        response = test_user.post('/api/v1/auth/login',
                                  data=json.dumps(test_sign_in),
                                  content_type='application/json')
        # import pdb; pdb.set_trace()
        self.token = response.json

    def tearDown(self):
        clear_user_table = "DELETE from users"
        cursor.execute(clear_user_table)
        clear_user_table = "DELETE from entries"
        cursor.execute(clear_user_table)

    def test_get_all_entries(self):
        test_user = app.test_client(self)
        test_user.post('/api/v1/entries', headers=self.token,
                       data=json.dumps(test_entry),
                       content_type='application/json')
        response = test_user.get(
            "/api/v1/entries", headers=self.token, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test content", str(response.data))

    def test_making_a_new_entry(self):
        test_user = app.test_client(self)
        response = test_user.post('/api/v1/entries', headers=self.token,
                                  data=json.dumps(test_entry),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("entry created", str(response.data))

    def test_getting_single_entry(self):
        test_user = app.test_client(self)
        test_user.post('/api/v1/entries', headers=self.token,
                       data=json.dumps(test_entry),
                       content_type='application/json')
        my_id = database.get_an_id()
        response = test_user.get('/api/v1/entries/{}'.format(my_id), headers=self.token,
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test content", str(response.data))

    def test_getting_non_existing_entry(self):
        test_user = app.test_client(self)
        response = test_user.get('/api/v1/entries/12', headers=self.token,
                                 content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn("no entry", str(response.data))

    def test_editing_an_entry(self):
        test_user = app.test_client(self)
        test_user.post('/api/v1/entries', headers=self.token,
                       data=json.dumps(test_entry),
                       content_type='application/json')
        my_id = database.get_an_id()
        response = test_user.put('/api/v1/entries/{}'.format(my_id), headers=self.token,
                                 data=json.dumps(test_entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("entry edited", str(response.data))

    def test_deleting_an_entry(self):
        test_user = app.test_client(self)
        test_user.post('/api/v1/entries', headers=self.token,
                       data=json.dumps(test_entry),
                       content_type='application/json')
        response = test_user.delete('/api/v1/entries/1', headers=self.token,
                                    data=json.dumps(test_entry),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("successfully deleted", str(response.data))

    def test_user_working_with_no_token(self):
        test_user = app.test_client(self)
        response = test_user.post('/api/v1/entries',
                                  data=json.dumps(test_entry),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("No auth token", str(response.data))

    def test_user_with_wrong_token(self):
        test_user = app.test_client(self)
        response = test_user.post('/api/v1/entries', headers={"token": "ddddd"},
                                  data=json.dumps(test_entry),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Invalid token", str(response.data))

    def test_editing_non_existing_entry(self):
        test_user = app.test_client(self)
        response = test_user.put('/api/v1/entries/1', headers=self.token,
                                 data=json.dumps(test_entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn("no such entry", str(response.data))


if __name__ == '__main__':
    unittest.main()
