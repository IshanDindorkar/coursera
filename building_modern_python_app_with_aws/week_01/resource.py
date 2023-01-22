"""
Script to test AWS SDK and use 'resource' feature to list down
all objects in S3 bucket
"""
import boto3
from loguru import logger


def main():
    s3 = boto3.resource("s3")
    bucket_name = "test-aws-sdk-bucket-2023"
    bucket = s3.Bucket(bucket_name)

    logger.info(f"The name of bucket is {bucket_name}")

    print("File Name | Modified Date | Size")
    print("===================================")
    for obj in bucket.objects.all():
        print(obj.key, obj.last_modified, obj.size)
    print("===================================")


if __name__ == "__main__":
    main()

