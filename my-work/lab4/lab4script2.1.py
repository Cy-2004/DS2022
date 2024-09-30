#!/usr/bin/python3

import urllib.request
import boto3

# create client
s3 = boto3.client('s3', region_name="us-east-1")

def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

image_url = "https://farmfreshfundraising.com/wp-content/uploads/2017/10/271156-grapes.jpg"
save_as = "grape.jpg"

download_image(image_url, save_as)

bucket = 'ds2022-gzd2yk'
local_file = 'grape.jpg'

with open(local_file, 'r') as file_data:
    resp = s3.put_object(
        Body = file_data,
        Bucket = bucket,
        Key = local_file
    )

bucket_name = 'ds2022-gzd2yk'
object_name = local_file
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )

print(response)
