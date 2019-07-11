""" Inintialisation file for tests"""
from config import Testing
from app import app

app.config.from_object(Testing)
#Test data
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
