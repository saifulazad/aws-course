import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('e-commerce')

try:
    response = table.put_item(
       Item={
            'attr_key': "order::ORD-3434",
            'sort_key': 'order_line::3',
            'placed_at': '2022-08-16',
            'qty': 2,
            'currency': 'BDT',
           'text': '1212'
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("PutItem succeeded:")
