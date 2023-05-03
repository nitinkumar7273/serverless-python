import os
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')


def create_todo_service(data):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
    }
    if table.put_item(Item=item):
        return 200
    else:
        return 404
