########### Get People Listed and Specific People Info ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json



# Subscription Key to identify my Service in Azure
subscription_key = '782aa30d07324ea8a0302092a34da569'


print("You will create a new person")
person = input("What's the name of the person?")
print("...................................")
groupid = input("What's the group id this person should belong to? ")
print("Creating a new person called" + person + " for the group " + groupid + "...")
print("...................................")

# Azure Data Center Region where my service is hosted / End Point
# 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/microsoft/persons'
group_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/'


# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json', }

# Request parameters for Face Detect

body = {
    "name": person,
}

params= { 'personGroupId': groupid }

# response = requests('post', group_url + group, body=body, headers=headers)
response = requests.post(group_url + groupid + '/persons', params=params, json=body, headers=headers)

# PRINT RAW FILE
print (response)

