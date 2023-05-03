import boto3

def lambda_handler(event, context):
  # update
  return {
    'statusCode': 200,
    'body': 'Hello World'
  }