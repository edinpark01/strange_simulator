import requests, urllib3

from urllib.parse import quote
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

usr = quote('USERNAME')
pwd = quote('PASSWORD')
proxy = 'YOUR_PROXY'
proxy_port = '8080'
proxy_http = 'http://' + usr + ':' + pwd + '@' + proxy + ':' + proxy_port
proxy_https = 'http://' + usr + ':' + pwd + '@' + proxy + ':' + proxy_port


session = requests.Session()
session.headers = {"Content-Type":"application/json"}
session.proxies = {
    "http": proxy_http,
    "https": proxy_https
}
session.verify = False
session.max_redirects = 150
session.trust_env = False
session.auth = (usr, pwd)
response = session.post(
    url="API_URL",
    json={"username": usr, "password": pwd}
)
print(response.json())
