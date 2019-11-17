########### Get People Listed and Specific People Info ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

# Subscription Key to identify my Service in Azure
subscription_key = 'XXXXXXXXXXXXXXXXXXXXX'


print(" - WARNING - ")
print("You Are Permanently Deleting a Person")
print("PERSON ID is required, this is not the person Name")
print("...............................")
personid = input("What is the person id you want to delete?  ")
print("...............................")
groupid = input(" What is the GroupID this person belongs to?  ")


# Azure Data Center Region where my service is hosted / End Point
# 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/microsoft/persons'
group_delete = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/' + groupid + '/persons/'
print(group_delete)

# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json', }

# Request parameters for Face Detect

params= { 'personGroupId': groupid, 'personId': personid }


print("Admin Code is Required to proceed")
admincode = input("Admin code? ")


if admincode == "rgdelete":
    response = requests.delete(group_delete + personid, params=params, headers=headers)
    print(response)          

else:
    print("Incorrect Code")
        










