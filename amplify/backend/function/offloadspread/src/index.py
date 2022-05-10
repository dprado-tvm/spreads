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