"""'
cognito utils
"""
import base64
import hashlib
import hmac

from commons.aws_constants import *


def get_secret_hash(secret_code):

    msg = secret_code + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'),
                   msg=str(msg).encode('utf-8'),
                   digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()
