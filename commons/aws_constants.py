"""
 contains all env variables
"""
import os

AWS_COGNITO = 'cognito-idp'
AWS_REGION = 'us-east-1'

AWS_ACCESS_KEY = os.getenv('IAM_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('IAM_SECRET_KEY')
USER_POOL_ID = os.getenv('COGNITO_USER_POOL_ID')
CLIENT_ID = os.getenv('COGNITO_USER_POOL_CLIENT_ID')
CLIENT_SECRET = os.getenv('COGNITO_USER_POOL_CLIENT_SECRET')
