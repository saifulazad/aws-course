import boto3
import time


# Define the function code
def lambda_handler(event, context):
    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')

    # Define the table name and item data
    table_name = 'users'
    item_data = {
        'email': {
            'S': 'mamun@gmail.com'
        },
        'datetime': {
            'S': str(int(time.time()))
        },
        # add other attributes here as needed
    }

    # Put the item into the table
    response = dynamodb.put_item(
        TableName=table_name,
        Item=item_data
    )
    return {
        'statusCode': 200,
        'body': response
    }


if __name__ == "__main__":
    x = lambda_handler([], [])
    print(x)
