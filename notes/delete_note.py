import os, json, boto3
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.getenv("NOTES_TABLE"))

def lambda_handler(event, ctx):
    note_id = event["pathParameters"]["id"]
    try:
        table.delete_item(Key={"noteId": note_id})
        return {"statusCode": 204, "body": ""}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
