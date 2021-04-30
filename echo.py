import json
import os


def lambda_handler(request, context):
    stage = os.environ["MY_STAGE"]
    author = os.environ["AUTHOR"]
    data = {
        'env': {
            'stage': stage,
            'author': author
        }
    }
    try:
        body = json.loads(request["body"])
        msg = body["msg"]
        code = 0
        message = 'SUCCESS'
        data['echo'] = msg
    except Exception as e:
        code = 4001
        message = 'FAILED'
        data['err'] = 'no msg received...'

    return {
        'statusCode': 200,
        'body': json.dumps({
            'code': code,
            'message': message,
            'data': data
        })
    }
