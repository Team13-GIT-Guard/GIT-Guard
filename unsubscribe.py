import boto
import boto.s3
import sys
from boto.s3.key import Key

def main():
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''

    bucket_name = AWS_ACCESS_KEY_ID.lower() + '-demo'
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)

    full_bucket = conn.get_bucket(bucket_name)
    for key in full_bucket.list():
        key.delete()

    print("\n\t----------Unsubscribed----------")

