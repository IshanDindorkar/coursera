"""
Script to list details of all dragons stored in JSON file on S3 bucket
"""
import json
from pprint import pprint

import boto3


def main():
    # Get S3 resource and meta client to
    # eventually get handle to System Storage Manager
    s3 = boto3.resource("s3").meta.client
    ssm = boto3.client("ssm")

    # Retrieve parameter values using SSM(Services Systems Manager) client
    # SSM service is used for managing parameters used across AWS services
    bucket_name = ssm.get_parameter(Name="dragon_data_bucket_name",
                                    WithDecryption=False)["Parameter"]["Value"]
    file_name = ssm.get_parameter(Name="dragon_data_file_name",
                                  WithDecryption=False)["Parameter"]["Value"]

    expression = "select * from s3object s"
    result = s3.select_object_content(
        Bucket=bucket_name,
        Key=file_name,
        ExpressionType="SQL",
        Expression=expression,
        InputSerialization={"JSON": {"Type": "Document"}},
        OutputSerialization={"JSON": {}}
    )

    for event in result["Payload"]:
        if "Records" in event:
            result = json.dumps(event["Records"]["Payload"].decode("utf-8"), indent=2)
            print(result)


if __name__ == "__main__":
    main()
