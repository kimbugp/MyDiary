# import unittest
# import psycopg2
# from api.v1.models import dbase

# from api import app
# db=dbase()
# class UserTests(unittest.TestCase):

#     def test_database_connect_exception(self):
#         self.assertRaises(psycopg2.DatabaseError,db)

#     def test_creating_entries_table(self):
#         db=dbase()
#         self.assertIn(db.create_entries_table(),2)
    
#     def test_creating_user_table(self):
#         db=dbase()
#         self.assertIn(db.create_user_table(),2)
    