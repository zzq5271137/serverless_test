import json
import os


def lambda_handler(request, context):
    stage = os.environ["MY_STAGE"]
    try:
        body = json.loads(request["body"])
        msg = body["msg"]
        return {
            'statusCode': 200,
            'body': json.dumps({
                'code': 0,
                'message': 'SUCCESS',
                'data': {
                    'stage': stage,
                    'echo': msg
                }
            })
        }
    except Exception as e:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'code': 4001,
                'message': 'FAILED',
                'data': {
                    'stage': stage,
                    'err': 'no msg received...'
                }
            })
        }
