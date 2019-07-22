from flask import current_app

from app.models.dbtasks import UserOperations

entries = [
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    },
    {
        "entry_content": "Test content",
        "entry_name": "Test name",
        "user_id": 18,
        "entry_date": "2019-07-22 14:53:00"
    }
]

users = [
    {
        "password": "sha256$PzLPkOz7$967ee89b8160ebc2b759a39fd0c5faa91c317b2fec0082eb1176df44568ebc90",
        "username": "peter",
        "user_id": 18,
        "email": "kimbugwe@gmail.com",
        "name": "Simon Peter"
    }
]


def seed_data():
    database = UserOperations()
    [database.seed_user(**item) for item in users]
    [database.make_an_entry(**item) for item in entries]