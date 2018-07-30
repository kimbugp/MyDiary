import unittest
from flask import Flask, jsonify, make_response, request
import sys
import json

from api import app
from api.v1.models import dbase
from api.v1.dbtasks import dboperations


class all_entries_test(unittest.TestCase):

    def test_get_all_entries(self):
        test_user = app.test_client(self)
        response = test_user.get(
            "/api/v1/entries", content_type="application/json")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
