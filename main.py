import os

from flask import Flask
from flask_cors import CORS

import psycopg2
from app.models.models import DATABASE
from app.utils import db
from config import app_config


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config.get(config))
    app.url_map.strict_slashes = False
    # add cors
    CORS(app)
    # bind app to db
    db.connect(app, psycopg2, auto_commit=True)

    # import views
    from app.views import auth, entries, others, profile  # noqa
    app.register_blueprint(auth)
    app.register_blueprint(entries)
    app.register_blueprint(profile)
    app.register_blueprint(others)

    return app