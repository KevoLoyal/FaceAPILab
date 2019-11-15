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

container_name = input("To what container will the file be uploaded? ")
print("WARNING - File Name must be unique")
print("Also add the extension")
print("***********************************************")
local_file_name = input("What is the name of the file to upload?  ")
#local_file_name = 'bloodseeker.jpg'

# Blob


try:
	block_blob_service = BlockBlobService(account_name=storage_account, account_key=blob_storage_key)

	# Variable for Blob Path in LINUX
    # \Users\Kevin\Desktop\image.jpg
	# Create a file in Documents to test the upload and download.
	#path_built = r'\photos\bloodseeker.jpg' 
	#print(path_built) 
	# full_path_to_file = path.join('photos/bloodseeker.jpg')

	# Create a file in Documents to test the upload and download.
	full_path_to_file = local_file_name
	

	# Upload the created file, use local_file_name for the blob name.
	block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)
	bloburl = block_blob_service.make_blob_url(container_name, local_file_name)
	print("Your Blob URL is: ")
	print(bloburl)  # Test Print URL
	print("Please keep it Save")

except Exception as ex:
    print('Exception:')
    print(ex)

