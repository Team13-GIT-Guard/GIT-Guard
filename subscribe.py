import boto
import boto.s3
import sys
from boto.s3.key import Key

def get_emails():
    emails = []
    number = int(raw_input("\n\t\tPlease specify how many email address you want to subscribe: "))
    for i in range(number):
        email = str(raw_input("\t\tPlease type in a email address: "))
        emails.append(email)
    return emails

def main():
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''

    bucket_name = AWS_ACCESS_KEY_ID.lower() + '-demo'
    time_bucket_name = AWS_ACCESS_KEY_ID.lower() + '-time'
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)

    time_full_bucket = conn.get_bucket(time_bucket_name)
    for key in time_full_bucket.list():
        key.delete()
        
    full_bucket = conn.get_bucket(bucket_name)
    for key in full_bucket.list():
        key.delete()

    bucket = conn.get_bucket(bucket_name)
    time_bucket = conn.get_bucket(time_bucket_name)

    emails = get_emails()

    for email in emails:
        k = Key(bucket)
        k.key = email
        k.set_contents_from_string(email)

    file = open("timerecord.txt")
    line = file.readline()
    j = Key(time_bucket)
    j.key = str(line)
    j.set_contents_from_string(str(line))

    print("\n\t----------Subscribed----------")

