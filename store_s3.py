import boto3

aws_access_key = "------------"        # replace with your actual access key
aws_secret_access_key = "--------"  # replace with your actual secret
bucket_name = "sentinel-pay-uploads"

# Initialize S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_access_key,
    region_name="eu-north-1"  # Your bucket region
)