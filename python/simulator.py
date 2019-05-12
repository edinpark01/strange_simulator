import threading
import os
import boto3
import time
import sys
import csv
from botocore.exceptions import ClientError


def create_report():
    fields = ['s3-region', 'ec2-region', 'file', 'upload-time']
    file_name = "results.csv"

    if not os.path.isfile(file_name):
        csv_file = open(file_name, "w")
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()


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


def aws_test(ak, sk, rn, bk, lp, fn):
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

        upload_time = int(round(elapsed_time * 1000))
        start_time = int(round(start * 1000))
        print("INFO:\t\tFile: {}\t\tUpload Time: {} milliseconds\t\tStart Time: {}".format(fn, upload_time, start_time))

        data = [{
            "s3-region": rn,
            "ec2-region": "us-east-1",  # TODO: Pass EC2 region
            "file": fn,
            "upload-time": upload_time
        }]

        with open("results.csv", 'a') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=['s3-region', 'ec2-region', 'file', 'upload-time'])
            writer.writerows(data)
    except ClientError as e:
        raise e
    except FileNotFoundError as fnf_error:
        raise fnf_error


def cohesity_test():
    pass


def run(data: dict):
    """
    TODO: Write doc string
    TODO: Write UnitTest
    """
    sample_dir = "./sample_data"

    if not os.path.isdir(sample_dir):
        raise Exception("EXCEPTION:\t\tSample Data directory does not exist")
    else:
        for root, dirs, files in os.walk(sample_dir):

            if len(files) == 0:
                print("EXCEPTION:\t\tCould not read any files")

            for file_name in files:
                threading.Thread(
                    target=aws_test,
                    name=file_name,
                    args=(  # TODO: ADD EC2 region info
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
        create_report()
        run(args)
    else:
        raise Exception("EXCEPTION:\tError while reading arguments | expected 4")
