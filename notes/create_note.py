import json
import os
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        note_id = str(uuid.uuid4())
        content = body.get('content')

        item = {
            'noteId': note_id,
            'content': content
        }

        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Note created", "noteId": note_id})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
