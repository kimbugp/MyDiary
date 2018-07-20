import unittest
import json
from app import get_all_entries

class all_entries_test(unittest.TestCase):
    def create_app(self):
        get_all_entries.config['TESTING'] = True
        return get_all_entries
    #test if all entries are displayed
    def display_all_entries(self):
        test = get_all_entries.test_client(self)
        response = test.get("/entries", content_type="application/json")
        assert b'1' in response.data
        assert b'3' in response.data