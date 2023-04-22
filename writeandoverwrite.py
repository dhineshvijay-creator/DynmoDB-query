import boto3
from boto3.dynamodb.conditions import Key
# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Set the item data
item_data = {
    'userExternal': 'Sathish',
    'cognito uuid': '0',
    'ccess': 'granted'
}

# Write the item to the table (creating a new item)
write_params = {
    'TableName': 'Adminlogin',
    'Item': {
        key: {'N': value} if key in ['cognito uuid'] else {'S': value} for key, value in item_data.items()
    }
}
dynamodb.put_item(**write_params)

# Update the item in the table (overwriting existing item)
# Update the item in the table (overwriting existing item)
update_params = {
    'TableName': 'Adminlogin',
    'Key': {
        'userExternal': {'S': 'Sathish'},
        'cognito uuid': {'N': '0'}
    },
    'ExpressionAttributeValues': {
        ':new_value': {'S': 'grant'}
    },
    'UpdateExpression': 'SET ccess = :new_value',
    # Remove the ConditionExpression or update it to match an existing item
    #'ConditionExpression': 'attribute_exists(partition_key_name)'
}
dynamodb.update_item(**update_params)

