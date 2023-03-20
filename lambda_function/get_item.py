import boto3

client = boto3.client('dynamodb', region_name='us-east-1')
response = client.get_item(
    Key={
        'email': {
            'S': 'mamun@gmail.com'
        },
        'datetime': {
            'S': '1679302764'
        },
    },
    TableName='users',
)

print(response['Item'])

