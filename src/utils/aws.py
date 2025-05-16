import boto3
import json
import os

from botocore.exceptions import ClientError
from dotenv import load_dotenv
from typing import Any, Dict, Optional

# Load environment variables from .env file
load_dotenv()

# Define the AWS class
class AWSUtil:
    def __init__(self, secret_name: str, region_name: Optional[str] = None):
        self.secret_name = secret_name
        self.region_name = region_name or os.getenv("AWS_REGION")
        self.session = boto3.session.Session()
        self.client = self.session.client(
            service_name="secretsmanager",
            region_name=self.region_name,
        )

    def get_secret(self) -> Dict[str, Any]:
        """Retrieve the secret from AWS Secrets Manager."""
        try:
            get_secret_value_response = self.client.get_secret_value(SecretId=self.secret_name)
            secret = get_secret_value_response["SecretString"]
            return json.loads(secret)
        except ClientError as e:
            raise e  # Handle exceptions as needed
        
    # Update the secret in AWS Secrets Manager
    def update_secret(self, secret_value: Dict[str, Any]) -> None:
        """Update the secret in AWS Secrets Manager."""
        try:
            self.client.update_secret(
                SecretId=self.secret_name,
                SecretString=json.dumps(secret_value),
            )
        except ClientError as e:
            raise e
        