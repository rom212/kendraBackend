import json
import boto3

client = boto3.client('kendra')

def handler(event, context):
    
    print(event['queryStringParameters']['query'])
    client = boto3.client('kendra')
    response = client.query(
    IndexId='a58229fb-d69a-44c6-9d2e-28ce4632a616',
    QueryText= event['queryStringParameters']['query']
    #QueryText= "In which AWS Regions is AWS Transit Gateway available?"
    )

    if len(response['ResultItems']) == 0:
        result = "No result"
    else:
        result = response['ResultItems'][0]['AdditionalAttributes'][1]['Value']['TextWithHighlightsValue']['Text']
    
    print("Query: ",event['queryStringParameters']['query'])
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
