from celery import Celery
import boto3


# Create a session
session = boto3.Session()

# Get credentials from the session
credentials = session.get_credentials()
credentials = credentials.get_frozen_credentials()

# Access key, secret key, and session token
access_key = credentials.access_key
secret_key = credentials.secret_key
session_token = credentials.token

# Configure Celery to use AWS SQS as the broker
app = Celery(
    'celery_fastapi',
    broker='sqs://{aws_access_key}:{aws_secret_key}@',
    backend=f'db+postgresql://{service_account}:{service_account_password}@db_host:db_port/db_name',
    include=['queue.tasks'],
)

# AWS SQS-specific configuration
app.conf.update(
    broker_transport_options={
        'region': 'us-east-1',
        'visibility_timeout': 3600,  # Timeout in seconds
        'polling_interval': 10,  # Polling interval in seconds
        'predefined_queues': {
            'celery': {
                'url': 'https://sqs.us-east-1.amazonaws.com/123456789012/celery',  # Replace with your SQS queue URL
                'access_key_id': access_key,
                'secret_access_key': secret_key,
                'session_token': session_token,
            },
        },
        'task_default_queue': 'celery',  # Default SQS queue name
        'sts_role_arn': 'arn:aws:iam::123456789012:role/your-role',  # Replace with your IAM role ARN
        'sts_token_timeout': 900
    },  
)

if __name__ == '__main__':
    app.start()