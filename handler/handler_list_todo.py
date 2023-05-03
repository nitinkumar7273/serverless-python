import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')


def list_handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    result = table.scan()
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }
    return response
