import boto3

#will import the key attributes
from boto3.dynamodb.conditions import Key

#defining the resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

#defining the table
table = dynamodb.Table('Brooklyn99_Season8')

#running the query using the episode number key E01
response = table.query(
    KeyConditionExpression=Key('Episode_Number').eq('E01')
)

print(response['Items'])

#deleting the table

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table_name = 'Brooklyn99_Season8'

table = dynamodb.Table('Brooklyn99_Season8')

table.delete()

print('Deleted table:', 'Brooklyn99_Season8')