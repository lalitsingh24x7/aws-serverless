# clients
import boto3

# local
from commons.aws_constants import (
    AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, AWS_COGNITO
)

# cognito client resource object
COGNITO_CLIENT = boto3.client(
    AWS_COGNITO, aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION
)

# DynamoDB resource boto3 object
DB_CLIENT = boto3.resource(
    'dynamodb', aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION
)

# SNS client resource object
SNS_CLIENT = boto3.client(
    "sns", aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)
