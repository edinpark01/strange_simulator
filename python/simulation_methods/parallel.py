def write(pf, sim, ak, sk, rn, bk, lp, fn, eu):
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
        ).client(service_name='s3', endpoint_url=eu, verify=False)

        start = time.time()
        client.upload_file(lp, bk, fn)
        elapsed_time = time.time() - start

        upload_time = int(round(elapsed_time * 1000))
        start_time = int(round(start * 1000))
        print("INFO:\t\tFile: {}\t\tUpload Time: {} milliseconds\t\tStart Time: {}".format(fn, upload_time, start_time))

        data = [{
            'platform': pf,
            'simulation': sim,
            "s3-region": rn,
            "ec2-region": "us-east-1",  # TODO: Pass EC2 region
            "file": fn,
            "upload-time": upload_time
        }]

        with open("results.csv", 'a') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=['platform', 'simulation', 's3-region', 'ec2-region', 'file', 'upload-time'])
            writer.writerows(data)
    except ClientError as e:
        raise e
    except FileNotFoundError as fnf_error:
        raise fnf_error

def read():
    pass