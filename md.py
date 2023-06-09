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
workspace_id = os.getenv("WORKSPACE")
deployment_id = os.getenv("DEPLOYMENT")


def send_request():
    # Request
    # GET https://portal-api.platform.quix.ai/deployments

    try:
        response = requests.get(
            url="https://portal-api.platform.quix.ai/deployments/" + deployment_id,
            params={
                "workspaceId": workspace_id,
            },
            headers={
                "Authorization": "Bearer " + token
            }
        )

        deployment = json.loads(response.content)
        print("status: ", deployment["status"] ) 
        # to check response with jq
        #print(json.dumps(json.loads(response.content)))

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        
send_request()
