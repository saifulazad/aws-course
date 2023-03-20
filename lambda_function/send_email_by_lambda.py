import boto3
from botocore.exceptions import ClientError

SENDER = 'admin@fractalslab.com'
RECIPIENT = 'muazzem.mamun@gmail.com'
CCADDRESSES = 'mr.saiful.azad@gmail.com'
SUBJECT = 'Subject of the email'
BODY_TEXT = 'Text of the email'
BODY_HTML = '<html><body><h3>Email Body</h3></body></html>'

CHARSET = 'UTF-8'

client = boto3.client('ses')


def lambda_handler(event, context):
    source = "{} <{}>".format("Fractalslab", SENDER)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
                'CcAddresses': [
                    CCADDRESSES,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=source,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(f"Email sent! Message ID: {response['MessageId']}")


if __name__ == "__main__":
    lambda_handler([], [])

