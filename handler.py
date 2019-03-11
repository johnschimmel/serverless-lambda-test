import json
import boto3


def hello(event, context):
    sqs = boto3.client('sqs')

    account_id = context.invoked_function_arn.split(":")[4]
    queue_url = "https://sqs.us-east-1.amazonaws.com/218148629849/lambda-test-queue"

    sqs_response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=5,
        MessageBody=('testing new message to sqs')
    )
    # sqs_response = sqs.send_message(
    #     QueueUrl=queue_url,
    #     DelaySeconds=5,
    #     MessageAttributes={
    #         'Title': {
    #             'DataType': 'String',
    #             'StringValue': 'The Whistler'
    #         },
    #         'Author': {
    #             'DataType': 'String',
    #             'StringValue': 'John Grisham'
    #         },
    #         'WeeksOn': {
    #             'DataType': 'Number',
    #             'StringValue': '6'
    #         }
    #     },
    #     MessageBody=(
    #         'Information about current NY Times fiction bestseller for '
    #         'week of 12/11/2016.'
    #     )
    # )


    # print(sqs_response['MessageId'])
    # sqs_response = '123'
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "sqs": sqs_response
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def receiver(event, context):
    body = {
      "message": "Hello SQS",
      "event": event
    }
    print(json.dumps(body))

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response