import json
import boto3
import os

indexid = os.environ['INDEX_ID']
client = boto3.client('kendra')

def handler(event, context):
    
    print(event['queryStringParameters']['query'])
    client = boto3.client('kendra')
    response = client.query(
    IndexId=indexid,
    QueryText= event['queryStringParameters']['query']
    )

    if len(response['ResultItems']) == 0:
        result = "No result"
    else:
        result = response['ResultItems'][0]['AdditionalAttributes'][1]['Value']['TextWithHighlightsValue']['Text']
    
    print("Query: ",event['queryStringParameters']['query'])
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'result': result})
    }

