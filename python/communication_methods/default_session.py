import boto3

def put_object():
    data = open('test.txt', 'rb')
s3 = boto3.client('s3')
s3.put_object(Bucket='bucket-name', Key='test.txt', Body=data)