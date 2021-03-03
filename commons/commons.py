""" common utils"""

import json

from commons.boto_utils import DB_CLIENT
from commons.lambda_logger import get_logger

logger = get_logger()


def user_id(event):
    return event.get('requestContext')['authorizer']['claims']['sub']


def dynamo_table(table_name):
    return DB_CLIENT.Table(table_name)


def db_client():
    return DB_CLIENT


def response(success=True, data=None, message=None, status=200, exception=None, error_message=None):

    if exception or error_message:
        status = 400
        message = exception.args[0] if exception else error_message
        success = False
    return {
        "statusCode": status,
        "body": json.dumps(
            {
                'success': success,
                'data': data,
                'message': message
            }
        )
    }
