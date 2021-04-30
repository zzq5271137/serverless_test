import json
import os


def lambda_handler(request, context):
    print(request)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'code': 0,
            'message': "SUCCESS",
        })
    }
