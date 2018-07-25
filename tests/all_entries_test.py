import unittest
from flask import Flask,jsonify,make_response,request
import sys
import json

from api import app
from api.v1.app import entries


app=Flask(__name__)
class all_entries_test(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    
    def setup(self):
        self.test_entry=[
            {
                'entry_id':'1',
                'entry_date':'25/10/1995 20:15',
                'entry_name':'Dummy Entry',
                'entry_content':'Test Content'
            },
            {
                'entry_id':'2',
                'entry_date':'25/10/1995 20:15',
                'entry_name':'Dummy Entry',
                'entry_content':'Test Content'
            },
            {
                'entry_id':'3',
                'entry_date':'25/10/1995 20:15',
                'entry_name':'Dummy Entry',
                'entry_content':'Test Content'
            },
        ]

    #test if all entries are displayed
    def test_get_all_entries(self):
        # Tests that all entries can be retrieved
        testing_user = app.test_client(self)
        response = testing_user.get("/api/v1/entries", content_type="application/json")
        assert b'1' in response.data
        assert b'3' in response.data

    def test_API_can_show_all_entries(self):
        user=app.test_client(self)
        response=user.get("/api/v1/entries")
        self.assertIn('1',str(response.data),msg="all entries valid")

    # def test_API_can_make_new_entry(self):
    #     # Tests for a new entry
    #     testing_user = app.test_client(self)
    #     response = testing_user.post('/api/v1/entries', data=json.dumps(self.test_entry[0]),
    #                                  content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(self.test_entry[0]['entry_name'], str(response.data),msg="No entry made")
    
    # def test_hello_world(self):
    #     testing_user = app.test_client(self)
    #     response =testing_user.get('/api/v1/')
    #     self.assertIn('hello',str(response.data))
    
    # def test_get_specific_entry(self):
    #     # Tests getting aspecific entry
    #     testing_user = app.test_client(self)
    #     # add test entry
    #     response = testing_user.post('/api/v1/entries', data=json.dumps(self.test_entry[0]),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Your memory entitled ' + self.test_entry[0]['title'] + ' has been saved', str(response.data))
    #     #view added entry
    #     id = {'entry_id': 1}
    #     response = testing_user.get('/api/v1/entries/{}'.format(id['entry_id']))
    #     self.assertEqual(response.status_code, 200)
    
    # def test_null_entry_(self):
    #     # api to fail if null entry
    #     testing_user = app.test_client(self)
    #     self.test_entry[0]['content'] = ''
    #     response = testing_user.put('/api/v1/entries/1', data=json.dumps(self.test_entry[0]),
    #                                 content_type='application/json')
    #     self.assertIn('Null entry', str(response.data))

        
if __name__ == '__main__':
    unittest.main()
