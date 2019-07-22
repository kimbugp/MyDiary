from app.fixtures.seeder import seed_data
from app.utils import db


def seed_database():
    print("\n \n Seeding database \n \n \n")
    clear_user_table = "DELETE from users CASCADE"
    db.cursor.execute(clear_user_table)
    seed_data()


def create_tables():
    db.create_user_table()
    db.create_entries_table()
