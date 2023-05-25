import os
import boto3
import json
import datetime
import uuid
import ast

def LambdaHandler(event,context):
    
    dynamodb = boto3.resource("dynamodb")
    tableName  = os.environ['APIDB']
    table = dynamodb.Table(tableName )
    Method = event["httpMethod"]

    if Method == "POST":
        
        EV = event["body"]
        # """ Convert to JSON string """
        js = json.dumps(EV)
        # """ Convert JSON string to Python Obj """
        dic = json.loads(js)
        # """ Extract Value from Dictionary """
        data = dic[0]['event1']['attr1']

        timestamp = datetime.datetime.now().isoformat()
        # https://dynobase.dev/dynamodb-python-with-boto3/#put-item
        table.put_item(
          Item={
                "Timestamp": timestamp,
                "attribute": "attr1",
                "value": data,
            }
        )
        ele={'Timestamp': timestamp, 'value': data}
        body=f"Data Successfully Enter:{ele}"


# https://dynobase.dev/dynamodb-python-with-boto3/#scan
    elif Method == "GET":
        response = table.scan()
        body = response['Items']
    
    
    elif Method == "DELETE":
            response = table.delete_item(
                Key={
                    "value": data
                }
            )
    
    response = {
        "statusCode": 200,
        "body": body,
        "isBase64Encoded": False
    }
    return response

    
            







    


