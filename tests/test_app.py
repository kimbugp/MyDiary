"""Module to test API"""
from tests.base import (get_an_entry, TestingClass,
                        create_an_entry, create_wrong_entry,
                        get_single_entry, no_existing_entry,
                        edit_entry, wrong_data,
                        delete_entry, no_token, edit_no_entry, wrong_token,
                        unittest, error_page, profile)


class all_entries_test(TestingClass):
    """Class to test entries"""

    def test_get_all_entries(self):
        """Method to test getting all entry"""
        create_an_entry(self.test_user)
        response = get_an_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test content", str(response.data))

    def test_making_a_new_entry(self):
        """Method to test making an entry"""
        response = create_an_entry(self.test_user)
        self.assertEqual(response.status_code, 201)
        self.assertIn("entry created", str(response.data))

    def test_mising_signup_parameter(self):
        """Method to test missing signup parameter"""
        response = create_wrong_entry(self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('parameter missing', str(response.data))

    def test_getting_single_entry(self):
        """Method to test getting single entry"""
        create_an_entry(self.test_user)
        response = get_single_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test content", str(response.data))

    def test_getting_non_existing_entry(self):
        """Method to test non existing entry"""
        response = no_existing_entry(self.test_user)
        self.assertEqual(response.status_code, 404)
        self.assertIn("no entry", str(response.data))

    def test_editing_an_entry(self):
        """Method to test editing an entry"""
        response = edit_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("entry edited", str(response.data))

    def test_missing_parameter(self):
        """Method to test missing parameter"""
        response = wrong_data(self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('parameter missing', str(response.data))

    def test_deleting_an_entry(self):
        """Method to test delelting entry"""
        response = delete_entry(self.test_user)
        self.assertEqual(response.status_code, 200)
        self.assertIn("successfully deleted", str(response.data))

    def test_user_working_with_no_token(self):
        """Method to test working with no token"""
        response = no_token(self.test_user)
        self.assertEqual(response.status_code, 401)
        self.assertIn("No auth token", str(response.data))

    def test_user_with_wrong_token(self):
        """Method to test working wrong token"""
        response = wrong_token(self.test_user)
        self.assertEqual(response.status_code, 401)
        self.assertIn("Invalid token", str(response.data))

    def test_editing_non_existing_entry(self):
        """Method to test editing non exisitng entry"""
        response = edit_no_entry(self.test_user)
        self.assertEqual(response.status_code, 404)
        self.assertIn("no such entry", str(response.data))

    def test_catching_general_404(self):
        """Method to test genral 404"""
        response = error_page(self.test_user)
        self.assertEqual(response.status_code, 404)

    def test_view_profile(self):
        """Method to test viewing user profile"""
        response = profile(self.test_user)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
