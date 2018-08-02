import unittest
from config import TestingConfig
from api import app
from api.v1.models import dbase
from api.v1.dbtasks import dboperations
#set up the configs
#
app.config.from_object(TestingConfig)

test_user_data = {
    "username": "peter",
    "name": "Simon Peter",
    "email": "kimbugwe@gmail.com",
    "password": "12345678"
}
test_sign_in = {
    "username": "peter",
    "password": "12345678"
}
test_entry = {
    "entry_name": "Test name",
    "entry_content": "Test content"
}
wrong_test_entry = {
    "entry_content": "Test content"
}
wrong_test_user_data = {
    "name": "Simon Peter",
    "email": "kimbugwe@gmail.com",
    "password": "12345678"
}
wrong_test_sign_in = {
    "username": "peter"
}
test_wrong_sign_in = {
    "username": "peter",
    "password": "12345"
}



#define mock data

#create base class with Api test class with setup and teardown and db connection

#hellper methods for repeated scenario code
