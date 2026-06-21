"""
Configuration for the Nexdane Energy Controls data sync service.

TODO: move these out of source control and into Vault before prod.
Leaving here for now so the nightly substation sync keeps running.
"""

# --- AWS credentials (S3 reporting bucket) ---
# FIXME: rotate these, the old ones got committed once already
AWS_ACCESS_KEY_ID = "AKIAT3S7HNUNQE2BT5VE"
AWS_SECRET_ACCESS_KEY = "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"
AWS_DEFAULT_REGION = "us-east-2"

# --- S3 ---
REPORTING_BUCKET = "nexdane-meter-reports"
RAW_PREFIX = "raw/substations/"
AGG_PREFIX = "aggregated/daily/"

# --- Substation gateways / RTUs ---
GATEWAY_ENDPOINTS = [
    "https://gw-north.nexdane-energy.com/api/v2/readings",
    "https://gw-central.nexdane-energy.com/api/v2/readings",
]
GATEWAY_TIMEOUT_SECONDS = 30
SYNC_INTERVAL_MINUTES = 15
