########### Blob Interaction ###########

import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

# Get all modules for the Blob Storage
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings
import os, uuid
from os import path  # Import OS Path Function


# Python Classes Involved
# BlobServiceClient: The BlobServiceClient class allows you to manipulate Azure Storage resources and blob containers.
# ContainerClient: The ContainerClient class allows you to manipulate Azure Storage containers and their blobs.
# BlobClient: The BlobClient class allows you to manipulate Azure Storage blobs.

# Info to Blob

blob_storage_key = 'MPcaH5oNp/+oNgexNGjSafKd4yl5Cxrnv/RlSEX+wNt4PYmCiT7CtHJ6at/5veg0705m70oS4xS35M6B/Y8rdA=='

connect_str = 'DefaultEndpointsProtocol=https;AccountName=cognitiveservicesblob;AccountKey=MPcaH5oNp/+oNgexNGjSafKd4yl5Cxrnv/RlSEX+wNt4PYmCiT7CtHJ6at/5veg0705m70oS4xS35M6B/Y8rdA==;EndpointSuffix=core.windows.net'

storage_account = 'cognitiveservicesblob'

container_name = "container1"

# Blob


try:
	connect_str = os.getenv('CONNECT_STR')
	print(connect_str)

except Exception as ex:
    print('Exception:')
    print(ex)