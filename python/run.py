import threading
import os
import boto3
import time
import sys
import csv
import urllib3
import argparse
from enum import Enum
from botocore.exceptions import ClientError
from cohesity_wrapper.cohesity import get_s3_keys

import upload_methods.individual_upload
import upload_methods.concurrent_upload
import upload_methods.parallel_upload

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Platform(Enum):
    cohesity = 1
    aws = 2

def create_report():
    fields = ['platform', 'simulation', 's3-region', 'ec2-region', 'file', 'upload-time']
    file_name = "results.csv"

    if not os.path.isfile(file_name):
        csv_file = open(file_name, "w")
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()


def get_arguments():
    """
    TODO: Write UnitTest
    TODO: Write DocStr
    TODO: Read https://blog.sicara.com/perfect-python-command-line-interfaces-7d5d4efad6a2
    """
    platform = str()
    data = {
        'platform': None,
        'simulation': None,
        'bucket_name': None,
        'region': None,
        'access_key': None,
        'secret_key': None,
        'cluster_url': None
        }

    for index, arg in enumerate(sys.argv):
        if arg in ['--platform', '-p'] and len(sys.argv) > index + 1:
            platform = sys.argv[index + 1]
            data['platform'] = platform
            del sys.argv[index]
            del sys.argv[index]       
    
    if platform.lower() == Platform.cohesity.name:
        for index, arg in enumerate(sys.argv):
            if arg in ['--bucket-name'] and len(sys.argv) > index + 1:
                data['bucket_name'] = sys.argv[index + 1]
            elif arg in ['--simulation'] and len(sys.argv) > index + 1:
                data['simulation'] = sys.argv[index + 1]
        cohesity_key_dict = get_s3_keys()
        data['access_key'] = cohesity_key_dict["access_key"]
        data['secret_key'] = cohesity_key_dict["secret_key"]
        data['cluster_url'] = "https://cohesitydemo:3000"
    elif platform.lower() == Platform.aws.name:
        for index, arg in enumerate(sys.argv):
            if arg in ['--bucket-name'] and len(sys.argv) > index + 1:
                data['bucket_name'] = sys.argv[index + 1]
            elif arg in ['--region'] and len(sys.argv) > index + 1:
                data['region'] = sys.argv[index + 1]
            elif arg in ['--access-key'] and len(sys.argv) > index + 1:
                data['access_key'] = sys.argv[index + 1]
            elif arg in ['--secret-key'] and len(sys.argv) > index + 1:
                data['secret_key'] = sys.argv[index + 1]
            elif arg in ['--simulation'] and len(sys.argv) > index + 1:
                data['simulation'] = sys.argv[index + 1]
    return data


def cohesity_test():
    """
        To be deleted.
        integrated to test_platform
    """
    cohesity_api_dict = get_s3_keys()
    cluster_url = "https://cohesitydemo:3000"
    view_name = "test-s3"

    s3 = boto3.Session(aws_access_key_id=cohesity_api_dict['access_key'],aws_secret_access_key=cohesity_api_dict['secret_key']
                        ).client(service_name="s3", endpoint_url=cluster_url, verify=False)

    try:
        s3.upload_file('../test.txt', view_name, 'test3')
    except Exception as e:
        print("Problem see", e)

    bucket = s3.list_objects_v2(Bucket=view_name)
    for content in bucket['Contents']:
        print(content)


def run(data: dict):
    """
    TODO: Write doc string
    TODO: Write UnitTest
    """
    sample_list = ["/tmp/sample_data/random"]

    for sample_dir in sample_list:
        if not os.path.isdir(sample_dir):
            exception = "Sample Data directory does not exist | {}".format(sample_dir)
            raise Exception(exception)
        else:
            for root, dirs, files in os.walk(sample_dir):

                if len(files) == 0:
                    raise Exception("Could not read any files")

                for file_name in files:
                    threading.Thread(
                        target=parallel_write(),
                        name=file_name,
                        args=(  # TODO: ADD EC2 region info
                            data['platform'],
                            data['simulation'],
                            data['access_key'],
                            data['secret_key'],
                            data['region'],
                            data['bucket_name'],
                            os.path.join(root, file_name),
                            file_name,
                            data['cluster_url']
                        )).start()


if __name__ == "__main__":
    args = get_arguments()
    print(args)


    # if args is not None:
    #     create_report()
    #     run(args)
    # else:
    #     raise Exception("Error while reading arguments | Expected 4")
    
    # test_platform(args['access_key'], args['secret_key'], args['region'], args['bucket_name'],
    #               './newtest.txt', 'newtest', args['cluster_url']) 