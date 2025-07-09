import os, json, boto3
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.getenv("NOTES_TABLE"))

def lambda_handler(event, ctx):
    note_id = event["pathParameters"]["id"]
    data = json.loads(event["body"] or "{}")

    try:
        table.update_item(
            Key={"noteId": note_id},
            UpdateExpression="SET #t = :t, #c = :c",
            ExpressionAttributeNames={"#t": "title", "#c": "content"},
            ExpressionAttributeValues={":t": data.get("title"), ":c": data.get("content")},
        )
        return {"statusCode": 200, "body": json.dumps({"message": "Note updated"})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
