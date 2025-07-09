import os, json, boto3
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.getenv("NOTES_TABLE"))

def lambda_handler(event, ctx):
    note_id = event["pathParameters"]["id"]
    try:
        resp = table.get_item(Key={"noteId": note_id})
        item = resp.get("Item")
        if not item:
            return {"statusCode": 404, "body": json.dumps({"error": "Not found"})}
        return {"statusCode": 200, "body": json.dumps(item)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
