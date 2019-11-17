########### Get People Listed and Specific People Info ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json



# Subscription Key to identify my Service in Azure
subscription_key = 'XXXXXXXXXXXXXXXXXXXXX'



print("You will create a new group")
group = input("What's your new group id? ")
print("Creating the group " + group + "...")


# Azure Data Center Region where my service is hosted / End Point
# 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/microsoft/persons'
group_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/'


# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json', }

# Request parameters for Face Detect
# body = { "name": "test" }
body = {
    "name": group,
    "recognitionModel": "recognition_02"
}

params= { 'personGroupId': group }

# response = requests('post', group_url + group, body=body, headers=headers)
response = requests.put(group_url + group, params=params, json=body, headers=headers)

# PRINT RAW FILE
print (response)

