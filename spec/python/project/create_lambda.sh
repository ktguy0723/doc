#!/bin/bash

source ./.env

# IAM_ROLE Example
# IAM_ROLE = arn:aws:iam::123456789012:role/lambda-role

aws lambda create-function --function-name my-function \
--runtime python3.8 --role $IAM_ROLE \
--handler main.lambda_handler --zip-file fileb://output/src.zip

