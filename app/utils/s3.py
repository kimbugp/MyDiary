import json
import os

import boto3
import botocore


def copy_to_bucket(data):
    ACCESS_ID = os.environ.get("ACCESS_KEY_ID")
    ACCESS_KEY = os.environ.get("ACCESS_KEY")
    BUCKET = os.environ.get("BUCKET_NAME")
    KEY = 'subscribers'

    connection = boto3.resource("s3", aws_access_key_id=ACCESS_ID,
                                aws_secret_access_key=ACCESS_KEY)
    final_data_string = format_data(connection, BUCKET, KEY, data)
    connection.Bucket(BUCKET).put_object(Key=KEY, Body=final_data_string)


def format_data(connection, bucket, key, data):
    try:
        bucker_instance = connection.Object(bucket, key)
        obj = bucker_instance.get()["Body"].read()
    except botocore.exceptions.ClientError as e:
        return json.dumps(data)
    return ','.join((obj.decode('utf-8'), json.dumps(data)))
