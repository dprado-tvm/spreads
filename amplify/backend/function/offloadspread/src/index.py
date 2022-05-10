import json
import boto3

client = boto3.client('dynamodb', region_name='us-west-2')

def handler(event, context):
  data = client.query(
    TableName='TVSpreads',
    IndexName='Symbol',
    KeyConditionExpression='#name = :value',
    ExpressionAttributeValues={
      ':value': {
        'S': 'shoes'
      }
    },
    ExpressionAttributeNames={
      '#name': 'name'
    }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response