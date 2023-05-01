#getting JSON module for JSON data dumps
import json

#getting boto3 library
import boto3

#allows us to get the date/time
from datetime import datetime

#defining sqs client and the url of the SQS queue
sqs = boto3.client('sqs', region_name='us-east-2')
queue_url = 'https://sqs.us-east-2.amazonaws.com/597503565311/lambdaq'

#creating our function, defining the current time variable and sending a message to SQS
def lambda_handler(event, context):
    current_time = datetime.now().strftime("%H:%M:%S")
    
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=current_time)
    
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }