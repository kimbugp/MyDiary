from app import db

def seed_database():
    print("\n \n Seeding database \n \n \n")


def create_tables():
    db.create_user_table()
    db.create_entries_table()
