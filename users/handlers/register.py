import json

from commons.aws_constants import (CLIENT_ID, USER_POOL_ID)
from commons.boto_utils import COGNITO_CLIENT
from commons.cognito_utils import get_secret_hash
from commons.commons import response

from handlers.sns_services import save_user_info

client = COGNITO_CLIENT


def sign_up(event, _):
    try:
        fields = json.loads(event.get('body'))

        user_attributes = [
            {
                "Name": "email",
                "Value": fields['email']
            },
            {
                "Name": "custom:first_name",
                "Value": fields.get("first_name")
            },
            {
                "Name": "custom:last_name",
                "Value": fields.get("last_name")
            }
        ]

        password = fields.get('password')

        email_hash = get_secret_hash(fields.get("email"))
        resp = client.sign_up(
            ClientId=CLIENT_ID,
            SecretHash=email_hash,
            Username=fields.get("email"),
            Password=password,
            UserAttributes=user_attributes
        )

        fields.pop("password")
        fields.update({'pk': resp['UserSub'], 'sk': resp['UserSub']})

        # Save user into dynamo db via sns
        save_user_info(fields)
        return response()

    except Exception as e:
        return response(exception=e)


def sign_in(event, _):
    try:
        data = json.loads(event.get('body'))

        username, password = data.get('username'), data.get('password')

        auth_info = client.admin_initiate_auth(
            UserPoolId=USER_POOL_ID,
            ClientId=CLIENT_ID,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': username,
                'SECRET_HASH': get_secret_hash(username),
                'PASSWORD': password,
            },
            ClientMetadata={
                'username': username,
                'password': password,
            }).get('AuthenticationResult')

        return response(data=auth_info)
    except Exception as e:
        return response(exception=e)
