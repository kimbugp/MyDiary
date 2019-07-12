import os

from flask import Flask
from main import create_app
app, db = create_app(os.environ.get('FLASK_ENV'))


# import views
from .views import auth, entries, profile, general_routes  # noqa

app.register_blueprint(auth)
app.register_blueprint(entries)
app.register_blueprint(profile)
