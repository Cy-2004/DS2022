#!/bin/bash

aws s3 cp apple.png s3://ds2022-gzd2yk/

aws s3 presign --expires-in 604800 s3://ds2022-gzd2yk/apple.png

# https://ds2022-gzd2yk.s3.amazonaws.com/apple.png?AWSAccessKeyId=AKIAX5ZI6DW6FMUKD7XL&Signature=YtEC5I9T411n5kUljF814T83TSs%3D&Expires=1728288175
