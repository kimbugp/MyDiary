import psycopg2
import psycopg2.extras
from api.v1.models import dbase

db=dbase()
cursor=db.cursor
class dboperations():

    def create_a_user(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        new_user = ("INSERT INTO users(username,name,email,password) VALUES(%s,%s,%s,%s)")
        cursor.execute(new_user, (self.username, self.name, self.email, self.password))

    def make_an_entry(self, user_id, entry_id, entry_date, entry_name, entry_content):
        self.entry_id = entry_id
        self.entry_name = entry_name
        self.entry_date = entry_date
        self.entry_content = entry_content
        self.user_id = user_id
        new_entry = ("INSERT INTO entries(entry_id,entry_date,entry_name,entry_content) VALUES(%s,%s,%s,%s,%s)")
        cursor.execute(new_entry,(self.entry_id, self.entry_date, self.entry_name, self.entry_content))
    
    def get_all_entries(self, user_id, entry_id, entry_date, entry_name, entry_content):
        self.entry_id = entry_id
        self.entry_name = entry_name
        self.entry_date = entry_date
        self.entry_content = entry_content
        self.user_id = user_id
        all_entries = ("SELECT * FROM entries WHERE user_id==", (self.user_id))
        cursor.execute(all_entries)

    def get_one_entries(self, user_id, entry_id, entry_date, entry_name, entry_content):
        self.entry_id = entry_id
        self.entry_name = entry_name
        self.entry_date = entry_date
        self.entry_content = entry_content
        self.user_id = user_id
        all_entries = (
            "SELECT * FROM entries WHERE user_id==%s AND entry_id==%s", (self.user_id, self.entry_id))
        cursor.execute(all_entries)

    def select_user(self,username):
        self.username=username
        user = (
            "SELECT * FROM users WHERE user_id==%s", (self.username))
        return user
        