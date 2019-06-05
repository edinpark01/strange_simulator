import os
import boto3


def hello():
    """
    This function is intended for ensuring importing works
    """
    print("Hello from communication_methods package")


def upload_file(local_path: str, file_name: str, configuration):
    threshold = None
    remote_path = configuration.simulation + "/" + file_name

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

        s3_client.upload_file(
            local_path,
            configuration.bucket_name,
            remote_path,
            Config=threshold)
    except Exception as e:
        raise e
