import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

# Subscription Key to identify my Service in Azure
subscription_key = 'XXXXXXXXXXXXXXXXXXXXX'

persongroup = 'microsoft'

# Azure Data Center End Point
detect_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'

# Azure Data Center End Point
identify_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/identify'

# Request headers.
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

image_url = input("What is the URL of the image to detect?  ")

print("***********************************************")
print("")

####################################

params_detect = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'recognitionModel': 'recognition_02',
}
####################################


response = requests.post(detect_api_url, params=params_detect,
                         headers=headers, json={"url": image_url})


#print(json.dumps(response.json()))
parsed = json.loads(response.text)

####################################

# To Extract the Face ID index from a Matrix that is into a list
parsed_matrix1 = parsed[0]
print(parsed_matrix1)
facedetectid = parsed_matrix1['faceId'] 

print("************************************")
print(" ")
print('Your Face ID assigned to the image detected was: ')
print(" ")
print('>>>>>>>>>>>>        ' + facedetectid + '        <<<<<<<<<<<<' )
