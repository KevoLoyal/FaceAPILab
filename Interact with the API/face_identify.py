import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

# Subscription Key to identify my Service in Azure
subscription_key = 'XXXXXXXXXXXXXXXXXXXXX'


persongroup = input("What is the group name?  ")
print("")

# Azure Data Center End Point
detect_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'

# Azure Data Center End Point
identify_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/identify'

# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

####################################

facedetectid = input("What is the Face ID you want to identify?  ")

print("***********************************************")
print("")

####################################

params_identify = {
    "PersonGroupId": persongroup,
    "faceIds": [facedetectid],
    "maxNumOfCandidatesReturned": 1,
    "confidenceThreshold": 0.7
}

####################################

response = requests.post(identify_api_url, headers=headers, json=params_identify)

####################################
#print(json.dumps(response.json()))
####################################

parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))
