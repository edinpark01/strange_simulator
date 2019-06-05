import sys
from enum import Enum


class Platform(Enum):
    cohesity = 1
    aws = 2


class Configuration:
    def __init__(self):
        self.platform = None
        self.access_key = None
        self.secret_key = None
        self.session_key = None
        self.threshold = False
        self.region = None
        self.bucket_name = None
        self.simulation = None
        self.sample_data_path = None
        self.method = None
        self.url = None
        self.communication = "write"

    def __repr__(self):
        return repr({
            "platform": self.platform,
            "access_key": self.access_key,
            "secret_key": self.secret_key,
            "session_key": self.session_key,
            "threshold": self.threshold,
            "region": self.region,
            "bucket_name": self.bucket_name,
            "simulation": self.simulation,
            "sample_data_path": self.sample_data_path,
            "method": self.method,
            "url": self.url,
            "communication": self.communication}
        )

    @staticmethod
    def hello():
        print("Hello from Configuration Class")


def handler():

    conf = Configuration()

    for index, arg in enumerate(sys.argv):
        if arg in ['--platform', '-p'] and len(sys.argv) > index + 1:
            conf.platform = sys.argv[index + 1].lower()
        elif arg in ['--method', '-m'] and len(sys.argv) > index + 1:
            conf.method = sys.argv[index + 1].lower()
        elif arg in ['--communication', '-c'] and len(sys.argv) > index + 1:
            conf.communication = sys.argv[index + 1].lower()
        elif arg in ['--sample_data_path'] and len(sys.argv) > index + 1:
            conf.sample_data_path = sys.argv[index + 1].lower()
        elif arg in ['--bucket-name'] and len(sys.argv) > index + 1:
            conf.bucket_name = sys.argv[index + 1]
        elif arg in ['--simulation'] and len(sys.argv) > index + 1:
                conf.simulation = sys.argv[index + 1]

    if conf.platform == Platform.cohesity.name:
        cohesity_key_dict = get_s3_keys()
        conf.access_key = cohesity_key_dict["access_key"]
        conf.secret_key = cohesity_key_dict["secret_key"]
        conf.url = "https://cohesitydemo:3000"
    elif conf.platform == Platform.aws.name:
        for index, arg in enumerate(sys.argv):
            if arg in ['--region'] and len(sys.argv) > index + 1:
                conf.region = sys.argv[index + 1]
            elif arg in ['--access-key'] and len(sys.argv) > index + 1:
                conf.access_key = sys.argv[index + 1]
            elif arg in ['--secret-key'] and len(sys.argv) > index + 1:
                conf.secret_key = sys.argv[index + 1]

    print("Input Args:", conf)

    return conf
