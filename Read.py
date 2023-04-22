import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Adminlogin')

response = table.query(
    KeyConditionExpression=Key('userExternal').eq('Sathish')
)

items = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.query(
        KeyConditionExpression=Key('userExternal').eq('Sathish'),
        ExclusiveStartKey=response['LastEvaluatedKey']
    )
    items.extend(response['Items'])

print(items)
