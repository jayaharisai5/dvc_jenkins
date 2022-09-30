#from feature_engineering import feature_engineering
import os
import pandas as pd 
import boto3
client = boto3.client('s3')

#data = feature_engineering()
#data = pd.read_csv("cleaned_data.csv")
def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name=file_name
    response=client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(response)

def dvc():
    upload_files("cleaned_data.csv", "mlops-storage1")
    os.system("git init")
    os.system("dvc init -f")
    os.system("dvc remote add -d dvc-remote s3://mlops-storage1/dvc")
    os.system("dvc add cleaned_data.csv")
    os.system("git add cleaned_data.csv.dvc .gitignore")
    print("dvc file is pushing to s3......")
    os.system("dvc push")
    print("done")


    print("Deleting the unwanted files......")
    os.remove("cleaned_data.csv")
    os.remove("cleaned_data.csv.dvc")
    print("DVC Done")