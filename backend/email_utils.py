import boto3
import os

def send_email(to, subject, body):
    ses = boto3.client('ses', region_name='us-east-1')
    ses.send_email(
        Source=os.environ['SES_SENDER'],
        Destination={"ToAddresses": [to]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}}
        }
    )
