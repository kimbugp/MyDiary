import json
from tests import *
from tests.base import *


class all_entries_test(TestingClass):

    def test_get_all_entries(self):
        create_an_entry(self.test_user)
        response = get_an_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test content", str(response.data))

    def test_making_a_new_entry(self):
        response = create_an_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("entry created", str(response.data))

    def test_mising_signup_parameter(self):
        response = create_wrong_entry(self.test_user)
        self.assertEqual(response.status_code, 401)
        self.assertIn('parameter missing', str(response.data))

    def test_getting_single_entry(self):
        create_an_entry(self.test_user)
        response = get_single_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test content", str(response.data))

    def test_getting_non_existing_entry(self):
        response = no_existing_entry(self.test_user)
        self.assertEqual(response.status_code, 404)
        self.assertIn("no entry", str(response.data))

    def test_editing_an_entry(self):
        response = edit_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("entry edited", str(response.data))
    
    def test_missing_parameter(self):
        response =wrong_data(self.test_user)
        self.assertEqual(response.status_code,401)
        self.assertIn('parameter missing', str(response.data))

    def test_deleting_an_entry(self):
        response=delete_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("successfully deleted", str(response.data))

    def test_user_working_with_no_token(self):
        response=no_token(self.test_user)
        self.assertEqual(response.status_code, 401)
        self.assertIn("No auth token", str(response.data))

    def test_user_with_wrong_token(self):
        response=wrong_token(self.test_user)
        self.assertEqual(response.status_code, 401)
        self.assertIn("Invalid token", str(response.data))

    def test_editing_non_existing_entry(self):
        response = edit_no_entry(self.test_user)
        self.assertEqual(response.status_code, 404)
        self.assertIn("no such entry", str(response.data))


if __name__ == '__main__':
    unittest.main()
