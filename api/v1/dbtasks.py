import psycopg2
import psycopg2.extras
from api.v1.models import dbase


class dboperations(dbase):

    def create_a_user(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.new_user = ("INSERT INTO users VALUES(%s,%s,%s,%s)",
                         (self.username, self.name, self.email, self.password))
        self.cursor.execute(self.new_user)

    def make_an_entry(self, user_id, entry_id, entry_date, entry_name, entry_content):
        self.entry_id = entry_id
        self.entry_name = entry_name
        self.entry_date = entry_date
        self.entry_content = entry_content
        self.user_id = user_id
        self.new_entry = ("INSERT INTO entries VALUES(%s,%s,%s,%s,%s)",
                          (self.entry_id, self.entry_date, self.entry_name, self.entry_content, self.user_id))
        self.cursor.execute(self.new_entry)

    def get_all_entries(self, user_id, entry_id, entry_date, entry_name, entry_content):
        self.entry_id = entry_id
        self.entry_name = entry_name
        self.entry_date = entry_date
        self.entry_content = entry_content
        self.user_id = user_id
        self.all_entries = (
            "SELECT * FROM entries WHERE user_id==%s", (self.user_id))
        self.cursor.execute(self.all_entries)

    def get_one_entries(self, user_id, entry_id, entry_date, entry_name, entry_content):
        self.entry_id = entry_id
        self.entry_name = entry_name
        self.entry_date = entry_date
        self.entry_content = entry_content
        self.user_id = user_id
        self.all_entries = (
            "SELECT * FROM entries WHERE user_id==%s AND entry_id==%s", (self.user_id, self.entry_id))
        self.cursor.execute(self.all_entries)

    