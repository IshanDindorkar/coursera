"""
Script to use AWS SDK and 'client' feature to list down files
in S3 bucket
"""


import boto3


def main():
    client = boto3.client("s3")

    bucket_name = "test-aws-sdk-bucket-2023"
    response = client.list_objects(Bucket=bucket_name)

    for content in response["Contents"]:
        obj_dict = client.get_object(Bucket=bucket_name, Key=content["Key"])
        print(content["Key"], obj_dict["LastModified"])


if __name__ == "__main__":
    main()
