#pretty self explanitory. It imports boto3.
import os
import boto3
from botocore.exceptions import ClientError

#this initializes DynamoDB using boto3.client
dynamodb = boto3.client('dynamodb')

#creating the table and defining the attributes
try:
    table = dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Episode_Number',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'Title_of_Episode',
                'AttributeType': 'S',
            }
        ],
        TableName='Brooklyn99_Season8', #naming the table
            KeySchema=[
                {
                    'AttributeName': 'Episode_Number',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'Title_of_Episode',
                    'KeyType': 'RANGE'
                }
            ],
    
            ProvisionedThroughput={ #if we want to add 10 items we need 10 WCUs
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
    
    )

    print("Table created successfully") #verification

except ClientError as e:
    print(e)

dynamodb = boto3.client('dynamodb')

try:
    create_table = dynamodb.batch_write_item(
    RequestItems = {
    "Brooklyn99_Season8":[
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E01"
                    },
                    "Title_of_Episode":{
                        "S":"The Good Ones (1)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E02"
                    },
                    "Title_of_Episode":{
                        "S":"The Lake House (2)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E03"
                    },
                    "Title_of_Episode":{
                        "S":"Blue Flu (3)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E04"
                    },
                    "Title_of_Episode":{
                        "S":"Balancing (4)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E05"
                    },
                    "Title_of_Episode":{
                        "S":"PB&J (5)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E06"
                    },
                    "Title_of_Episode":{
                        "S":"The Set Up (6)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E07"
                    },
                    "Title_of_Episode":{
                        "S":"Game of Boyles (7)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E08"
                    },
                    "Title_of_Episode":{
                        "S":"Renewal (8)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E09"
                    },
                    "Title_of_Episode":{
                        "S":"The Last Day Pt 1 (9)"
                    }
                }
            }
        },
        {
            "PutRequest":{
                "Item":{
                    "Episode_Number":{
                        "S":"E10"
                    },
                    "Title_of_Episode":{
                        "S":"The Last Day Pt 2 (10)"
                    }
                }
            }
        }
    ]
}
)

except ClientError as e:
    print(e)

print("Ten items added!")