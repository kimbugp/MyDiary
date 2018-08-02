import unittest
import json
from tests import *
from tests.base import *

class UserTests(TestingClass):

    def test_user_signup(self):
        response = user_create(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn('User created', str(response.data))

    def test_user_signup_wrong(self):
        response = wrong_user(self.test_user)
        self.assertEqual(response.status_code, 401)
        self.assertIn('parameter missing', str(response.data))

    def test_user_already_exists(self):
        user_create(self.test_user)
        response =user_create(self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('User already exists', str(response.data))

    def test_can_login_user(self):
        response=user_create(self.test_user)
        self.assertEqual(response.status_code, 200)
    
    def test_user_cant_login_with_wrong_details(self):
        response = wrong_details(self.test_user)
        self.assertIn('parameter missing', str(response.data))

    def test_wrong_user_login(self):
        response=wrong_sign_in(self.test_user)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid login', str(response.data))

    # def test_invalid_password(self):
    #     test_user = app.test_client(self)
    #     test_user.post("/api/v1/auth/signup",
    #                    data=json.dumps(test_user_data), content_type="application/json")
    #     response = test_user.post('/api/v1/auth/login',
    #                               data=json.dumps(test_wrong_sign_in),
    #                               content_type='application/json')
    #     self.assertEqual(response.status_code, 401)
    #     self.assertIn('Check your login', str(response.data))

    def test_hello_world(self):
        response = helo(self.test_user)
        self.assertIn('hello', str(response.data))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
