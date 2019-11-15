########### Create Face for Person ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json



# Subscription Key to identify my Service in Azure
subscription_key = '782aa30d07324ea8a0302092a34da569'




print("You will add a new face to a person")
groupid = input("What's the Group id this person belongs to? ")
print("...................................")
print(" ")
personid = input("What's the Person ID you will add the face to?  ")
print("...................................")
print(" ")
imageurl = input("What is the URL of the image?  ")
print("...................................")
print(" ")
print("Creating a new face for " + personid + "...")

# Azure Data Center Region where my service is hosted / End Point
# 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/microsoft/persons'
group_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/' + groupid + '/persons/' + personid + '/persistedFaces'


# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json', 'detectionModel': 'detection_02' }

# Request parameters for Face Detect

body = {
    "url": imageurl
}

params= { 'personGroupId': groupid, 'personId': personid }

# response = requests('post', group_url + group, body=body, headers=headers)
response = requests.post(group_url, params=params, json=body, headers=headers)

# PRINT RAW FILE
# print (response)

parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))

