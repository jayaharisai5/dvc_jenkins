#import requied libraries
import pandas as pd
import boto3 
import botocore
from configparser import ConfigParser

file = "cred\cred.ini"
config = ConfigParser()
config.read(file)

session = boto3.Session(
         aws_access_key_id=config["account"]["aws_access_key_id"],
         aws_secret_access_key=config["account"]["aws_secret_access_key"]
)
'''
s3 = boto3.resource('s3')
try:
    s3.Bucket("mlops-storage1").download_file('hari/bank.csv', 'bank.csv')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
'''
def load_data():
    client = boto3.client('s3')
    path = 's3://mlops-storage1/hari/bank.csv'
    df=pd.read_csv(path)
    print("Data is loaded......")
    return df

