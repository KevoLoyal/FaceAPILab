########### Create Face for Person ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json



# Subscription Key to identify my Service in Azure
subscription_key = '782aa30d07324ea8a0302092a34da569'




print("You will proceed to train the group")
groupid = input("What's the Group id this person belongs to? ")
print(" ")
print("...................................")
print(" ")
print("Training the group " + groupid + "...")

# Azure Data Center Region where my service is hosted / End Point
# 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/microsoft/persons'
group_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/' + groupid + '/train' 


# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json', }

# Request parameters for Face Detect

body = {}

params= { 'personGroupId': groupid, }

# response = requests('post', group_url + group, body=body, headers=headers)
response = requests.post(group_url, params=params, json=body, headers=headers)

# PRINT RAW FILE
print (response)


