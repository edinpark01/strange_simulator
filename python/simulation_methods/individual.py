import os
import communication_methods


def write(conf):
    """
        This function traverses a specified local directory
        and uses a custom session upload wrapper to upload each
        file in the directory up to bucket/view depending on which
        platform being tested.
        The key here is that it individually uploads each file, and
        only moves on to the next file in the directory after it has
        finished uploading the current file.
    """
    try:
        for root, dirs, files in os.walk(conf.sample_data_path):
            for file_name in files:
                local = os.path.join(root, file_name)
                communication_methods.custom_session.upload_file(conf, local, file_name)
    except Exception as e:
        raise e


def read(conf):
    try:
        communication_methods.custom_session.download_file(conf)
    except Exception as e:
        raise e
