"""Module to perform database tasks"""

import psycopg2
from app.utils import db


class BaseOperations():
    def __init__(self):
        self.cursor = db.cursor
        self.dict_cursor = db.dict_cursor


class UserOperations(BaseOperations):
    """Class to perform database operations"""

    def create_a_user(self, username, name, email, password):
        """Method to create a user"""
        new_user = (
            "INSERT INTO users(username,name,email,password)\
                                 VALUES(%s,%s,%s,%s)")
        self.cursor.execute(new_user, (username, name,
                                       email, password))

    def make_an_entry(self, user_id, entry_date, entry_name, entry_content):
        """Method to create an entry"""
        new_entry = (
            "INSERT INTO entries(entry_date,entry_name,entry_content,user_id)\
                                 VALUES(%s,%s,%s,%s) RETURNING entry_id")
        self.dict_cursor.execute(new_entry, (entry_date,
                                             entry_name, entry_content,
                                             user_id))
        entry = self.dict_cursor.fetchone()
        return entry

    def get_all_entries(self, user_id):
        """Method to get all entries"""
        all_entries = (
            "SELECT entry_id,entry_date,entry_name,entry_content FROM entries \
            WHERE user_id='{}'".format(user_id))
        self.dict_cursor.execute(all_entries)
        data = self.dict_cursor.fetchall()
        return data

    def get_one_entry(self, user_id, entry_id):
        """Method to get onne entry"""
        all_entries = (
            "SELECT entry_id,entry_date,entry_name,entry_content FROM entries\
             WHERE entry_id={} AND user_id='{}'"
            .format(entry_id, user_id))
        self.dict_cursor.execute(all_entries)
        entries = self.dict_cursor.fetchone()
        return entries

    def get_an_id(self):
        """Method to get a user id"""
        entry_id = ("select * from entries")
        self.dict_cursor.execute(entry_id)
        my_id = self.dict_cursor.fetchone()
        return my_id['entry_id']

    def edit_one_entry(self, user_id, entry_id, entry_name, entry_content, *args, **kwargs):
        """Method to edit an entry"""
        edit_entries = (
            "UPDATE entries SET entry_name= %s, entry_content= %s WHERE \
            entry_id= %s AND user_id='{}' and entry_date>current_date and \
            entry_date<current_date+1".format(user_id))
        self.cursor.execute(edit_entries, (entry_name,
                                           entry_content, str(entry_id)))

    def select_user(self, username):
        """Method to check a user"""
        signin = ("SELECT * FROM users WHERE username='{}'"
                  .format(username))
        self.dict_cursor.execute(signin)
        user = self.dict_cursor.fetchall()
        return user

    def verify_new_user(self, username, email):
        """Method to verify a user"""
        signin = (
            "SELECT * FROM users WHERE username='{}' \
            or email='{}'".format(username, email))
        self.dict_cursor.execute(signin)
        user = self.dict_cursor.fetchall()
        return user

    def delete_entry(self, user_id, entry_id):
        """Method to delete an entry"""
        delete = ("DELETE FROM entries WHERE entry_id={} and \
                  user_id='{}'".format(
            entry_id, user_id))
        self.cursor.execute(delete)
        return 'successfully deleted'

    def select_user_id(self, user_id):
        """Method to get a user-id"""
        signin = ("SELECT * FROM users WHERE user_id='{}'"
                  .format(user_id))
        self.dict_cursor.execute(signin)
        user = self.dict_cursor.fetchall()
        return user
    
    def seed_user(self, user_id, username, name, email, password):
        """Method to seed a user"""
        new_user = (
            "INSERT INTO users(user_id,username,name,email,password)\
                                 VALUES(%s,%s,%s,%s,%s)")
        self.cursor.execute(new_user, (user_id, username, name,
                                       email, password))


class Profile(BaseOperations):
    def get_profile(self, user_id):
        """Method to get user profile"""
        profile = ('''select username,email,name,count(entries.user_id)\
                   ,profession,profilepic from users left join entries\
                   on entries.user_id=users.user_id where users.user_id={}\
                   group by users.user_id''').format(user_id)
        self.dict_cursor.execute(profile)
        user = self.dict_cursor.fetchall()
        return user

    def edit_profile(self, user_id, profession):
        """Method to profile edit"""
        pic = ('''UPDATE users SET profession='{}' where user_id={}''').format(
            profession, user_id)
        self.cursor.execute(pic)
