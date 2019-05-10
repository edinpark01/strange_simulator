import threading
import os
import boto3
import json
import time


def upload(local, remote, fn, reg):
    with open('aws_info.json') as json_file:
        data = json.load(json_file)
        error = False

        try:
            session = boto3.Session(
                aws_access_key_id=data['aws_access_key_id'],
                aws_secret_access_key=data['aws_secret_access_key'],
                region_name=reg
            )
        except:
            error = True
            print("EXCEPTION:\tError while initializing Session")
            print("\t\t\tRegion => {}".format(data["region_name"]))

        try:
            client = session.client(service_name='s3')
        except:
            error = True
            print("EXCEPTION:\tError while initializing client")

        try:
            print("INFO:\t\tFile: {}\t\tUploading...".format(fn))
            start = time.time()
            client.upload_file(local, data['bucket_name'], remote)
            end = time.time()
        except:
            error = True
            print("EXCEPTION:\tError while uploading file: {}".format(fn))
            print("\t\t=> Bucket: {}".format(data['bucket_name']))

        if not error:
            print("INFO:\t\tFile: {}\t\tUpload Time: {} milliseconds".format(fn, (int(round((end - start) * 1000)))))

        return local


def run(region):
    sample_dir = "sample_data"

    if not os.path.isdir(sample_dir):
        print("EXCEPTION:\t\tSample Data directory does not exist")
    else:
        for root, dirs, files in os.walk(sample_dir):

            if len(files) == 0:
                print("EXCEPTION:\t\tCould not read any files")

            for file_name in files:
                local_path = os.path.join(root, file_name)
                s3_path = os.path.relpath(local_path, ".")

                threading.Thread(target=upload, args=(local_path, s3_path, file_name, region)).start()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("EXCEPTION:\t\tMissing EC2 instance region")
    else:
        run(sys.argv[1])
