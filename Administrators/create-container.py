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

blob_storage_key = 'KEY STRING'

connect_str = 'CONNECTION STRING'

storage_account = 'Account Name'

print("WARNING - Container name must be unique")
container_name = input("Container name to create: ")

# Blob


try:
	block_blob_service = BlockBlobService(account_name=storage_account, account_key=blob_storage_key)

	block_blob_service.create_container(container_name)

	block_blob_service.set_container_acl(
    container_name, public_access=PublicAccess.Container)

except Exception as ex:
    print('Exception:')
    print(ex)

print("Container Created Correctly")
