#!/usr/bin/env python3.7
import os
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('Brooklyn99_Season8')

#now to scan the table
response = table.scan()

#will store the scan in this variable
items = response['Items']

for item in items:
    print(item)

print("Scan completed successfully.")
