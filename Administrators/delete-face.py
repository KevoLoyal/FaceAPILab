########### Get People Listed and Specific People Info ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

# Subscription Key to identify my Service in Azure
subscription_key = '782aa30d07324ea8a0302092a34da569'


print(" - WARNING - ")
print("You Are Permanently Deleting a Person's face")
print("...............................")
print(" ")
groupid = input(" What is the GroupID this person belongs to?  ")
print("...............................")
print(" ")
print("PERSON ID is required, this is not the person Name")
print(" ")
personid = input("What is the person id you want to delete?  ")
print("...............................")
print(" ")
faceid = input("What is face id you want to permanently delete?  ")
print("...............................")


# Azure Data Center Region where my service is hosted / End Point
# 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/microsoft/persons'
face_delete = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/' + groupid + '/persons/' + personid + '/persistedFaces/'

# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json', }

# Request parameters for Face Detect

params= { 'personGroupId': groupid, 'personId': personid, 'persistedFaceId': faceid, }


print("Admin Code is Required to proceed")
admincode = input("Admin code? ")


if admincode == "rgdelete":
    response = requests.delete(face_delete + personid, params=params, headers=headers)
    print(response)          

else:
    print("Incorrect Code")
        










