import psycopg2
import psycopg2.extras
from api.v1.models import dbase

db = dbase()
cursor = db.cursor
dict_cursor = db.dict_cursor


class dboperations():

    def create_a_user(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        new_user = (
            "INSERT INTO users(username,name,email,password) VALUES(%s,%s,%s,%s)")
        cursor.execute(new_user, (self.username, self.name,
                                  self.email, self.password))

    def make_an_entry(self,entry_date, entry_name, entry_content):
        self.entry_name = entry_name
        self.entry_date = entry_date
        self.entry_content = entry_content
        new_entry = (
            "INSERT INTO entries(entry_date,entry_name,entry_content) VALUES(%s,%s,%s)")
        cursor.execute(new_entry, (self.entry_date,
                                   self.entry_name, self.entry_content))

    def get_all_entries(self):
        all_entries = (
            "SELECT entry_id,entry_date,entry_name,entry_content FROM entries")
            # WHERE user_id={}".format(self.user_id)
        dict_cursor.execute(all_entries)
        data = dict_cursor.fetchall()
        return data

    def get_one_entry(self, entry_id):
        self.entry_id = str(entry_id)
        all_entries = (
            "SELECT entry_id,entry_date,entry_name,entry_content FROM entries WHERE entry_id={}".format(self.entry_id))
        dict_cursor.execute(all_entries)
        entries = dict_cursor.fetchall()
        return entries

    def edit_one_entry(self, entry_name, entry_content, entry_id):
        self.entry_name = entry_name
        self.entry_id = str(entry_id)
        self.entry_content = entry_content
        edit_entries = (
            "UPDATE entries SET entry_name= %s, entry_content= %s WHERE entry_id= %s")
        cursor.execute(edit_entries, (self.entry_name,
                                      self.entry_content, self.entry_id))

    def select_user(self,username):
        self.username =username
        signin = ("SELECT * FROM users WHERE username={}".format(self.username))
        dict_cursor.execute(signin)
        user=dict_cursor.fetchall()
        return user

    def delete_entry(self,entry_id):
        self.entry_id=entry_id
        delete=("DELETE FROM entries WHERE entry_id={}".format(self.entry_id))
        cursor.execute(delete)
        return 'successfully deleted'