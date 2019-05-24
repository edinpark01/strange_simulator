import requests
import os
import urllib3
from urllib.parse import quote

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = os.environ['COHESITY_USERNAME']
password = os.environ['COHESITY_PASSWORD']
base_url = os.environ['COHESITY_BASE_URL']

def get_access_token():
    """
        This function takes a username and password for
        the Cohesity system and and returns the authorization
        token for subsequent api calls.
    """
    headers = {"Content-Type": "application/json"}
    json = {"domain": "local",
            "username": username,
            "password": password
            }
    url = base_url + "public/accessTokens"
    print('Getting Token now.')
    req = requests.post(url=url, headers=headers, json=json, verify=False)

    request_data = req.json()
    return request_data['accessToken']


def get_s3_keys():
    """
        This function takes no arguments, will first try 
        and get authorization token, then if successful
        will send an api request to get s3 tokens.  
    """
    try:
        authorization_token = "Bearer " + get_access_token()
    except Exception as e:
        raise e
    headers = {"Content-Type": "application/json",
               "Authorization": authorization_token}
    url = base_url + "public/sessionUser"
    print('Getting S3 Tokens.')
    req = requests.get(url=url, headers=headers, verify=False)

    request_data = req.json()
    token_dict = {"access_key": request_data['s3AccessKeyId'],
                  "secret_key": request_data['s3SecretKey']}

    return token_dict

if __name__ == "__main__":
    print(get_s3_keys())
