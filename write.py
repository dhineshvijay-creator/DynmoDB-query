import boto3

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Set the write parameters
write_params = {
    'TableName': 'Adminlogin',
    'Item': {
        'userExternal': {'S': 'Sathish'},
        'cognito uuid': {'N': '0'},
        'Access': {'S': 'denied'}
    },
    'ConditionExpression': 'attribute_not_exists(partition_key_name)' # Optional condition to prevent overwriting existing items
}

# Execute the write operation
try:
    response = dynamodb.put_item(**write_params)
    print('Write succeeded:', response)
except dynamodb.exceptions.ConditionalCheckFailedException as e:
    print('Write failed due to condition check:', e)
except Exception as e:
    print('Write failed:', e)
