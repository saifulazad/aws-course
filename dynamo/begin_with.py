import boto3, json
from boto3.dynamodb.conditions import Key

# boto3 is the AWS SDK library for Python.
# The "resources" interface allows for a higher-level abstraction than the low-level client interface.
# For more details, go to http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('e-commerce')

resp = table.query(KeyConditionExpression=Key('attr_key').eq('order::ORD-3434') & Key('sort_key').begins_with('order_line::'))

print("The query returned the following items:")
for item in resp['Items']:
    print(item)
