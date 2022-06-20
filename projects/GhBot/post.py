from github.config import GhConfig
from github.loggers import Logger
import requests as req
import argparse
import json

parser = argparse.ArgumentParser(description="POST request for GhBot")
version='1.0.0'

#Version
parser.add_argument('-v', action='version', version=version)
parser.add_argument('-u', type = str,help = "Your github username")

args = parser.parse_args()
username = args.u

dev_url= GhConfig.API.PROD_URL
endpoint = GhConfig.API.ENDPOINT


url = GhConfig.buildURL(dev_url,endpoint)

post_content = { "text":username }
data = {'content': post_content}
headers = {'Content-type': 'application/json'}

res = req.post(url, data=json.dumps(post_content), headers=headers)
if res.status_code == 200:
    Logger.success("Request sent successfully")
    Logger.info(json.dumps(res.json(),indent=6))