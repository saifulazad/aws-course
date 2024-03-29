import boto3, json, decimal

from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table('e-commerce')

try:
    response = table.get_item(
        Key={
            'attr_key': "#profile-mr.saiful.azad@gmail.com",
            'sort_key': "#profile"
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("GetItem succeeded:")
    print(json.dumps(response['Item'], indent=4, cls=DecimalEncoder))
