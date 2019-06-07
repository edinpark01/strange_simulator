import os
import boto3
import time


def hello():
    """
    This function is intended for ensuring importing works
    """
    print("Hello from communication_methods package")


def log_results(start, end, file_name):
    start = int(round(start * 1000))
    end = int(round(end * 1000))
    elapsed = end - start

    print("INFO:\tFilename: {}\tStart time: {}\tDuration: {}"
          "".format(file_name, start, elapsed))


def session_wrapper(conf, file=None):
    threshold = None

    if conf.threshold:
        stat_info = os.stat(file)
        size = stat_info.st_size
        threshold = TransferConfig(multipart_threshold=size+1)

    session = boto3.Session(
        aws_access_key_id=conf.access_key,
        aws_secret_access_key=conf.secret_key,
        aws_session_token=conf.session_key,
        region_name=conf.region)

    s3_client = session.client(
        service_name='s3',
        verify=False,
        endpoint_url=conf.url)

    return s3_client, threshold


def upload_file(conf, local_path: str, file: str):
    client, thresh = session_wrapper(conf, file)
    remote_path = configuration.simulation + "/" + file

    try:
        start = time.time()
        s3_client.upload_file(local_path, conf.bucket_name, remote_path, Config=thresh)
        end = time.time()

        log_results(start, end, remote_path)
    except Exception as e:
        raise e


def download_file(configuration):
    client, thresh = session_wrapper(configuration)

    try:
        bucket = client.list_objects_v2(
            Bucket=configuration.bucket_name,
            Prefix=configuration.simulation)

        os.system("mkdir -p /tmp/download/" + configuration.simulation)

        for content in bucket['Contents']:
            f = open('/tmp/download/' + content['Key'], 'w').close()

            start = time.time()
            client.download_file(
                Bucket=configuration.bucket_name,
                Key=content['Key'],
                Filename='/tmp/download/' + content['Key'])
            end = time.time()

            log_results(start, end, content['Key'])
    except Exception as e:
        raise e
