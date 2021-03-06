########### Get People Listed and Specific People Info ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

# Subscription Key to identify my Service in Azure
subscription_key = 'XXXXXXXXXXXXXXXXXXXXX'



# Azure Data Center Region where my service is hosted / End Point
# 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/microsoft/persons'
facelist_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/'


# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

# Request parameters for Face Detect
params= {
    'top': '20',
}

response = requests.get(facelist_url, params=params, headers=headers)

# PRINT RAW FILE
#print(json.dumps(response.json()))

# PRINT PARSED FILE
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))
