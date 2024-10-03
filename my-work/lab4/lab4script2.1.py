#!/usr/bin/python3

import urllib.request
import boto3

# create client
s3 = boto3.client('s3', region_name="us-east-1")

#def download_image(url, save_as):
  #try:
    #urllib.request.urlretrieve(url, save_as)
  #except Exception as e:
    #print(e)

#image_url = "https://farmfreshfundraising.com/wp-content/uploads/2017/10/271156-grapes.jpg"
#save_as = "grape.jpg"

#download_image(image_url, save_as)

#with open(local_file, 'rb') as file_data:
resp = s3.put_object(
    Body = "grape.jpg",
    Bucket = "ds2022-gzd2yk",
    Key = "grape.jpg",
    ACL = 'public-read',
)

bucket_name = 'ds2022-gzd2yk'
object_name = "grape.jpg"
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )

print(response)

# presigned url: https://ds2022-gzd2yk.s3.amazonaws.com/grape.jpg?AWSAccessKeyId=AKIAX5ZI6DW6FMUKD7XL&Signature=cxB0itTdk15fq8gnOxN%2BWye%2FfQM%3D&Expires=1728576510
