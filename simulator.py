import threading
import os
import boto3
import json
import time


def upload(local, remote, fn):
    with open('aws_info.json') as json_file:
        data = json.load(json_file)

        session = boto3.Session(
            aws_access_key_id=data['aws_access_key_id'],
            aws_secret_access_key=data['aws_secret_access_key'],
            region_name=data["region_name"]
        )

        client = session.client(service_name='s3')

        start = time.time()
        client.upload_file(local, data['bucket_name'], remote)
        end = time.time()

        print("File: {}\t\tUpload Time: {} milliseconds".format(fn, (int(round((end - start) * 1000)))))

        return local_path


for root, dirs, files in os.walk("./sample_data/"):

    for file_name in files:
        local_path  = os.path.join(root, file_name)
        s3_path     = os.path.relpath(local_path, ".")

        threading.Thread(target=upload, args=(local_path, s3_path, file_name)).start()
