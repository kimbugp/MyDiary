import json
import os

import requests
from flask import Blueprint, jsonify, make_response, request, redirect
from jsonschema import ValidationError as Error

import boto3
from app.utils.error_handlers import ValidationError
from app.utils.s3 import copy_to_bucket
import textwrap
others = Blueprint("errors", __name__)


@others.route("/")
def index():
    """
    End Point for the index page
    """
    data = f'''client_id={os.environ.get('JOBS_SLACK_CLIENT_ID')}&client_secret={os.environ.get('JOBS_SLACK_CLIENT_SECRET')}&code={request.args.get('code')}'''
    res = requests.post(
        "https://slack.com/api/oauth.access",
        data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response_json = res.json()
    if response_json.get("ok") is False:
        return redirect('https://slack.com/400', code=302)
    copy_to_bucket(response_json.get("incoming_webhook"))
    team = response_json.get('incoming_webhook').get(
        'configuration_url').split('.slack.com')[0]
    return redirect(team + '.slack.com', code=302)


@others.app_errorhandler(404)
def page_not_found(e):
    """
    End Point to catch 404s
    """
    return make_response(jsonify({"message": "Page not found"})), 404


@others.app_errorhandler(ValidationError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@others.app_errorhandler(Error)
def handle_invalid_input(error):
    response = jsonify({"error": error.message})
    response.status_code = 400
    return response
