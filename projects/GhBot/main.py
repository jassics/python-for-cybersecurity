from github.bot import GhBot
from github.loggers import Logger
import argparse
import json

parser = argparse.ArgumentParser(description="POST request for GhBot")
version='1.0.0'

#Version
parser.add_argument('-v', action='version', version=version)
parser.add_argument('-u', type = str,help = "Your github username")

args = parser.parse_args()
username = args.u

bot = GhBot()
data_dict,status,msg = bot.serve(content=username)
output = {
    "status": status,
    "message": msg,
    "data": data_dict
}

Logger.info(json.dumps(output,indent=6))