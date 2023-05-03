import json
import logging

from service.service_create_todo import create_todo_service


def create_handler(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item")

    else:
        create_todo = create_todo_service(data)
        if create_todo == 200:
            response = {
                "statusCode": 200,
                "body": json.dumps("Todo added")
            }
            return response
        else:
            response = {
                "statusCode": 404,
                "body": json.dumps("Failed to add Todo")
            }
            return response
