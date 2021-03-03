"""SNS module"""
import os
import json

from commons.boto_utils import SNS_CLIENT


def save_user_info(data_dict):

    sns_client = SNS_CLIENT

    sns_client.publish(
        TargetArn=os.getenv('SNS_DB_ARN'),
        Message=json.dumps({'default': json.dumps(data_dict)}),
        MessageStructure='json'
    )
