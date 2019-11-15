########### Blob Interaction ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

# Get all modules for the Blob Storage
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings
from os import path  # Import OS Path Function


# Python Classes Involved
# BlobServiceClient: The BlobServiceClient class allows you to manipulate Azure Storage resources and blob containers.
# ContainerClient: The ContainerClient class allows you to manipulate Azure Storage containers and their blobs.
# BlobClient: The BlobClient class allows you to manipulate Azure Storage blobs.

# Info to Blob

blob_storage_key = 'MPcaH5oNp/+oNgexNGjSafKd4yl5Cxrnv/RlSEX+wNt4PYmCiT7CtHJ6at/5veg0705m70oS4xS35M6B/Y8rdA=='

connect_str = 'DefaultEndpointsProtocol=https;AccountName=cognitiveservicesblob;AccountKey=MPcaH5oNp/+oNgexNGjSafKd4yl5Cxrnv/RlSEX+wNt4PYmCiT7CtHJ6at/5veg0705m70oS4xS35M6B/Y8rdA==;EndpointSuffix=core.windows.net'

storage_account = 'cognitiveservicesblob'

container_name = input("To what container you want to list? ")
print("***********************************************")
# local_file_name = input("What is the name of the file to upload?  ")

try:
	block_blob_service = BlockBlobService(account_name=storage_account, account_key=blob_storage_key)
	generator = block_blob_service.list_blobs(container_name)	

except Exception as ex:
    print('Exception:')
    print(ex)

for blob in generator:
    print(blob.name)