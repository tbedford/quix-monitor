# Install the Python Requests library:
# `pip install requests`

import requests
import json
import time
from datetime import datetime
import os
from dotenv import load_dotenv
import sys

load_dotenv()
token = os.getenv("TOKEN")


def send_request():
    # Request
    # GET https://portal-api.platform.quix.ai/deployments

    try:
        response = requests.get(
            url="https://portal-api.platform.quix.ai/deployments",
            params={
                "workspaceId": "tonybedford-workspace1",
            },
            headers={
                "Authorization": "Bearer "+token
            }
        )

        deployments = json.loads(response.content)

        for d in deployments:

            print('{name}  --  {status}'.format(name=d["name"], status = d["status"]))
            
        # print(json.dumps(json.loads(response.content)))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        

while True:
    print(datetime.now())
    send_request()
    print('----------------------------------------------')
    sys.stdout.flush() # to use with `tail -f` or `less +F`
    time.sleep(3)
