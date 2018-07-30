import psycopg2
from psycopg2.extras import RealDictCursor


class dbase():

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                "dbname=diarydb user=postgres password=qwertyuiop")
            self.cursor = self.conn.cursor()
            self.dict_cursor = self.conn.cursor(
                cursor_factory=RealDictCursor)
            self.conn.autocommit = True
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_user_table(self):
        user_table = ("CREATE TABLE IF NOT EXISTS users"
                      "(id serial  NOT NULL PRIMARY KEY,"
                      "username VARCHAR(50) NOT NULL,"
                      "name VARCHAR(50) NOT NULL,"
                      "email VARCHAR(80) NOT NULL,"
                      "password VARCHAR(200) NOT NULL)")
        self.cursor.execute(user_table)

    def create_entries_table(self):
        entries_table = ("CREATE TABLE IF NOT EXISTS entries"
                         "(entry_id serial  NOT NULL PRIMARY KEY,"
                         "entry_date TIMESTAMP NOT NULL,"
                         "entry_name VARCHAR(50) NOT NULL,"
                         "entry_content VARCHAR(80) NOT NULL,"
                         "user_id VARCHAR(200))")

        self.cursor.execute(entries_table)


if __name__ == '__main__':
    db = dbase()
    db.create_entries_table()
    db.create_user_table()
