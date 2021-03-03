import json
from commons import commons
from commons.commons import response


def user_profile(event, _):
    pk = commons.user_id(event)
    data = commons.dynamo_table('users').get_item(
        Key={
            'pk': pk,
            'sk': pk
        }
    ).get('Item')
    return response(data=data)
