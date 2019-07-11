import os

from flask import Flask
from main import create_app

app = create_app(os.environ.get('FLASK_ENV'))


# import views
from .views import home