import os
import boto3
import time

def hello():
    """
    This function is intended for ensuring importing works
    """
    print("Hello from communication_methods package")


def upload_file(local_path: str, remote_path: str, configuration):
    threshold = None

    if configuration.threshold:
        stat_info = os.stat(file)
        size = stat_info.st_size
        threshold = TransferConfig(multipart_threshold=size+1)

    try:
        session = boto3.Session(
            aws_access_key_id=configuration.access_key,
            aws_secret_access_key=configuration.secret_key,
            aws_session_token=configuration.session_key,
            region_name=configuration.region)

        s3_client = session.client(
            service_name='s3',
            verify=False,
            endpoint_url=configuration.url)

        start = int(round( time.time() * 1000 ))
        s3_client.upload_file(local_path, configuration.bucket_name,
                             remote_path, Config=threshold)
        elaspsed = int(round( time.time() * 1000 )) - start

        print("INFO:\tFilename: {}\tStart time: {}\tUpload time: {}".format(remote_path, start, elaspsed))

    except Exception as e:
        raise e
