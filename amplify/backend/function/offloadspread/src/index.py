import json
import boto3
from boto3.dynamodb.conditions import Key

client = boto3.client('dynamodb', region_name='us-west-2')

def handler(event, context): 
  def query():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('TVSpreads')      

    resp = table.query(
      KeyConditionExpression=Key('Symbol').eq('SPXm')
    )
    
    for item in resp['Items']:
      print(item)
      
    return {
        "statusCode": 200,
        "body": json.dumps(item),
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Content-Type": "application/json",
        },
    }