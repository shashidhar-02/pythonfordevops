import boto3
client=boto3.client('s3')
resource=client.create_bucket(
    Bucket='shashifor345',
)
print(resource)