import threading
import os
import boto3
import time
import sys
from botocore.exceptions import ClientError


def get_arguments():
    # TODO: Write UnitTest
    # TODO: Write DocStr
    # TODO: Read https://blog.sicara.com/perfect-python-command-line-interfaces-7d5d4efad6a2
    if len(sys.argv) is not 5:
        return None
    else:
        return {
            "access_key": sys.argv[1],
            "secret_key": sys.argv[2],
            "region": sys.argv[3],
            "bucket_name": sys.argv[4]
        }


def upload(ak, sk, rn, bk, lp, fn):
    """
    TODO: Write doc string
    TODO: Write UnitTest
    """

    try:  # TODO: One try and multiple exceptions | READ https://botocore.amazonaws.com/v1/documentation/api/latest/client_upgrades.html#error-handling
        print("INFO:\t\tFile: {}\t\tUploading...".format(fn))

        client = boto3.Session(
            aws_access_key_id=ak,
            aws_secret_access_key=sk,
            region_name=rn
        ).client(service_name='s3')

        start = time.time()
        # client.upload_file(lp, bk, fn)
        elapsed_time = time.time() - start

    except ClientError as e:
        raise e
    else:
        milli_secs = int(round(elapsed_time * 1000))
        print("INFO:\t\tFile: {}\t\tUpload Time: {} milliseconds".format(fn, milli_secs))


def run(data: dict):
    """
    TODO: Write doc string
    TODO: Write UnitTest
    """
    sample_dir = "./sample_data"

    if not os.path.isdir(sample_dir):
        print("EXCEPTION:\t\tSample Data directory does not exist")
    else:
        for root, dirs, files in os.walk(sample_dir):

            if len(files) == 0:
                print("EXCEPTION:\t\tCould not read any files")

            for file_name in files:
                threading.Thread(
                    target=upload,
                    name=file_name,
                    args=(
                        data['access_key'],
                        data['secret_key'],
                        data['region'],
                        data['bucket_name'],
                        os.path.join(root, file_name),
                        file_name
                    )).start()


if __name__ == "__main__":
    args = get_arguments()

    if args is not None:
        run(args)
    else:
        print("EXCEPTION:\tError while reading arguments | expected 4")
