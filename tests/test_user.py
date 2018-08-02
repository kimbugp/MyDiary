"""Module to test login/signup user activity """
import unittest
from tests.base import (TestingClass, user_create, wrong_user,
                        helo, wrong_details, wrong_sign_in,
                        user_create_token,user)


class UserTests(TestingClass):
    """Class to test endpoints"""

    def test_user_signup(self):
        """Method to test signup"""
        response = user_create(self.test_user)
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created', str(response.data))

    def test_user_signup_wrong(self):
        """Method to test wrong signup"""
        response = wrong_user(self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('parameter missing', str(response.data))

    def test_user_already_exists(self):
        """Method to test existing user"""
        user_create(self.test_user)
        response = user_create(self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('User already exists', str(response.data))

    def test_can_login_user(self):
        """Method to test signin"""
        response = user(self.test_user)
        self.assertEqual(response.status_code, 200)

    def test_user_cant_login_with_wrong_details(self):
        """Method to test sign in with wrong detail"""
        response = wrong_details(self.test_user)
        self.assertIn('parameter missing', str(response.data))

    def test_wrong_user_login(self):
        """Method to test sign in with wrong detail"""
        response = wrong_sign_in(self.test_user)
        self.assertEqual(response.status_code, 403)
        self.assertIn('Invalid login', str(response.data))

    def test_hello_world(self):
        """Method to test hello world"""
        response = helo(self.test_user)
        self.assertIn('hello', str(response.data))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
