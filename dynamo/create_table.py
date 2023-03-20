import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Define the table schema
table_name = 'users'
key_schema = [
    {
        'AttributeName': 'email',
        'KeyType': 'HASH'  # Partition key
    },
    {
        'AttributeName': 'datetime',
        'KeyType': 'RANGE'  # Sort key
    }
]
attribute_definitions = [
    {
        'AttributeName': 'email',
        'AttributeType': 'S'  # S stands for String type
    },
    {
        'AttributeName': 'datetime',
        'AttributeType': 'S'  # S stands for String type
    }
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,   # Number of read capacity units to be reserved for this table
    'WriteCapacityUnits': 5   # Number of write capacity units to be reserved for this table
}

# Create the table
dynamodb.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=attribute_definitions,
    ProvisionedThroughput=provisioned_throughput
)
