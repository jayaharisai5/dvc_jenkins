#import requied libraries
import pandas as pd
import boto3 
import botocore



session = boto3.Session(
         aws_access_key_id="AKIA3YG72WSKAY3DQARO",
         aws_secret_access_key="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"
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

