"""
Nightly sync: pull substation/RTU readings from gateways, push aggregates to S3.
"""
import boto3
import requests
import config


def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        region_name=config.AWS_DEFAULT_REGION,
    )


def fetch_readings(endpoint):
    resp = requests.get(endpoint, timeout=config.GATEWAY_TIMEOUT_SECONDS)
    resp.raise_for_status()
    return resp.json()


def upload_aggregate(s3, key, body):
    s3.put_object(Bucket=config.REPORTING_BUCKET, Key=key, Body=body)


def run():
    s3 = get_s3_client()
    for endpoint in config.GATEWAY_ENDPOINTS:
        readings = fetch_readings(endpoint)
        key = config.AGG_PREFIX + "latest.json"
        upload_aggregate(s3, key, str(readings))
        print(f"synced {len(readings)} readings from {endpoint}")


if __name__ == "__main__":
    run()
