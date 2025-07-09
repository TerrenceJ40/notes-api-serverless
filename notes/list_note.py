import os, json, boto3
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.getenv("NOTES_TABLE"))

def lambda_handler(event, ctx):
    try:
        items = table.scan()["Items"]
        return {"statusCode": 200, "body": json.dumps(items)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
