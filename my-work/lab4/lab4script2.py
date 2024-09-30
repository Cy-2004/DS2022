#!/usr/bin/python3

import boto3

# create client
s3 = boto3.client('s3', region_name="us-east-1")

# make request
#response = s3.list_buckets()

# now iterate through the response:
#for r in response['Buckets']:
  #print(r['Name'])

bucket = 'ds2022-gzd2yk'
local_file = 'orange.png'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file,
    ACL = 'public-read',
)

