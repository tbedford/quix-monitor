# `pip install requests`
# `pip install vonage`

import requests
import json
import time
import os
import sys
import vonage
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
workspace_id = os.getenv("WORKSPACE")
deployment_id = os.getenv("DEPLOYMENT")
brand_name = os.getenv("VONAGE_BRAND_NAME")
to_number = os.getenv("TO_NUMBER")
vonage_key = os.getenv("VONAGE_API_KEY")
vonage_secret = os.getenv("VONAGE_API_SECRET")

# Request
# GET https://portal-api.platform.quix.ai/deployments
def send_request():
    
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
        if deployment["status"] != "Running":
            client = vonage.Client(key=vonage_key, secret=vonage_secret)
            sms = vonage.Sms(client)
            responseData = sms.send_message(
                {
                    "from": brand_name,
                    "to": to_number,
                    "text": "Alert: Quix Sentinel notices deployment id  " + deployment_id + " status not Running.",
                }
            )

            if responseData["messages"][0]["status"] == "0":
                print("Message sent successfully. Admin Alerted. Exiting.")
                exit(-1)
            else:
                print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        
while True:
    print(datetime.now())
    send_request()
    time.sleep(4)

