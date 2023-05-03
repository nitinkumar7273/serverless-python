1. To deploy the service:
    # serverless deploy

2. To test handler 'handler_crete_todo'(POST):
    - events to pass:
        # event = {
            "body": '{"text": "Todo 1"}'
        }
    - To test local:
        # serverless invoke local --function create

3. To test handler 'handler_create_todo'(GET) .i.e to get all the todos:
    - To test local:
        # serverless invoke local --function list