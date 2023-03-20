import boto3

# create a boto3 client for Amazon Rekognition
rekognition = boto3.client('rekognition')


# define the Lambda function
def lambda_handler(event, context):
    # get the S3 bucket and key for the image from the event
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    # use Amazon Rekognition to detect celebrities in the image
    response = rekognition.recognize_celebrities(Image={'S3Object': {'Bucket': s3_bucket, 'Name': s3_key}})

    # extract the list of celebrities and their confidence scores
    celebrities = response['CelebrityFaces']
    results = [{'Name': c['Name'], 'Confidence': c['MatchConfidence']} for c in celebrities]
    print(results)
    # return the results
    return results


if __name__ == "__main__":
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "fractalslab-internal",
                    },
                    "object": {
                        "key": "jeff_bezos.jpg",
                    }
                }
            }
        ]
    }
    lambda_handler(event=event, context=[])


