import json

from commons.boto_utils import DB_CLIENT
from commons.commons import response


def insert_data(data):
    table = DB_CLIENT.Table('users')
    table.put_item(
        Item=data
    )


def save_user(event, _):
    try:
        message_data = str(event['Records'][0]['Sns']['Message'])
        message_data = json.loads(message_data)
        insert_data(message_data)
        return response()

    except Exception as e:
        return response(exception=e)
