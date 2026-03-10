import boto3
import pandas as pd
import os
from datetime import datetime

# AWS credentials (from your IAM user)
aws_access_key_id = "------------"        # replace with your actual access key
aws_secret_access_key = "--------"  # replace with your actual secret
region_name = "eu-north-1" 

# Bucket name
bucket_name = "sentinel-pay-uploads"

# Path to processed transactions
file_path = os.path.join(os.path.dirname(__file__), "../Processing/processed_transactions.csv")
# Load CSV
df = pd.read_csv(file_path)

# Filter flagged transactions
flagged = df[df['flag'].isin(["High Value", "Impossible Travel"])]

# Initialize S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Upload flagged transactions
for i, row in flagged.iterrows():
    filename = f"{row['user_id']}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    s3.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=row.to_json(),
        ContentType='application/json'
    )
    print(f"Uploaded {filename} to S3")