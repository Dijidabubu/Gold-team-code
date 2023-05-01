#!/bin/usr/env/Gold-team-code python3.7

#import boto3
import boto3

#define variable as sqs
sqs = boto3.client('sqs')

#creating the new Q
response = sqs.create_queue(
    QueueName='lambdaq'
)

#confirmation
print('SQS Q created')
print(response)