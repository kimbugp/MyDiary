import unittest
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
wrong_test_user_data = {
    "name": "Simon Peter",
    "email": "kimbugwe@gmail.com",
    "password": "12345678"
}
test_sign_in = {
    "username": "peter",
    "password": "12345678"
}
wrong_test_sign_in = {
    "username": "peter"
}
test_wrong_sign_in = {
    "username": "peter",
    "password": "12345"
}


class UserTests(unittest.TestCase):

    def tearDown(self):
        clear_user_table = "DELETE from users"
        cursor.execute(clear_user_table)

    def test_user_signup(self):
        test_user = app.test_client(self)
        response = test_user.post(
            "/api/v1/auth/signup", data=json.dumps(test_user_data), content_type="application/json")
        response2=test_user.post(
            "/api/v1/auth/signup", data=json.dumps(wrong_test_user_data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn('User created', str(response.data))
        self.assertEqual(response2.status_code,401)
        self.assertIn('parameter missing', str(response2.data))
    def test_user_already_exists(self):
        test_user = app.test_client(self)
        test_user.post("/api/v1/auth/signup",
                       data=json.dumps(test_user_data), content_type="application/json")
        response = test_user.post(
            "/api/v1/auth/signup", data=json.dumps(test_user_data), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn('User already exists', str(response.data))

    def test_can_login_user(self):
        test_user = app.test_client(self)
        test_user.post("/api/v1/auth/signup",
                       data=json.dumps(test_user_data), content_type="application/json")
        response = test_user.post('/api/v1/auth/login',
                                  data=json.dumps(test_sign_in),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Token', str(response.data))
        response2 = test_user.post('/api/v1/auth/login',
                                  data=json.dumps(wrong_test_sign_in),
                                  content_type='application/json')
        self.assertEqual(response2.status_code,401)
        self.assertIn('parameter missing', str(response2.data))

    def test_wrong_user_login(self):
        test_user = app.test_client(self)
        response = test_user.post('/api/v1/auth/login',
                                  data=json.dumps(test_sign_in),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid login', str(response.data))

    def test_invalid_password(self):
        test_user = app.test_client(self)
        test_user.post("/api/v1/auth/signup",
                       data=json.dumps(test_user_data), content_type="application/json")
        response = test_user.post('/api/v1/auth/login',
                                  data=json.dumps(test_wrong_sign_in),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Check your login', str(response.data))

    def test_hello_world(self):
        testing_user = app.test_client(self)
        response = testing_user.get('/', content_type="application/json")
        self.assertIn('hello', str(response.data))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
