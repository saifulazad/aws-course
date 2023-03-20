import boto3


def lambda_handler(event, context):
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
    return {
        'statusCode': 200,
        'body': response['Item']
    }


if __name__ == "__main__":
    x = lambda_handler([], [])
    print(x)

