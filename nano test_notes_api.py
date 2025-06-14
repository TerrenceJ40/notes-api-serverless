import boto3
import requests
from requests.auth import AuthBase
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import InstanceMetadataProvider, InstanceMetadataFetcher
from botocore.session import Session

# Replace with your API Gateway invoke URL (no trailing slash)
api_url = "https://your-api-id.execute-api.region.amazonaws.com/Prod"

# Custom Auth class to sign requests with SigV4
class SigV4AuthWrapper(AuthBase):
    def __init__(self, service, region):
        session = Session()
        creds = session.get_credentials()
        self.sigv4 = SigV4Auth(creds, service, region)

    def __call__(self, request):
        aws_request = AWSRequest(method=request.method, url=request.url, data=request.body, headers=request.headers)
        self.sigv4.add_auth(aws_request)
        request.headers.update(dict(aws_request.headers.items()))
        return request

# Use this auth for your request
auth = SigV4AuthWrapper("execute-api", "us-east-1")  # Change region if different

# Test GET request to /notes
response = requests.get(f"{api_url}/notes", auth=auth)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
