# nexdane-backend

Data sync service for the Nexdane Energy Controls SCADA/metering platform.
Pulls readings from substation RTUs and regional gateways, aggregates them,
and syncs to our S3 reporting bucket for the ops dashboard.

Internal tooling — Nexdane Energy Controls Ltd.

## Setup

​```bash
pip install -r requirements.txt
python s3_sync.py
​```

## Configuration

Connection settings and credentials live in `config.py`.
See `.env.example` for the expected environment variables.

## Status

- [x] RTU / gateway ingest
- [x] S3 sync
- [ ] Move secrets to Vault (TODO before prod — still hardcoded in config.py)
- [ ] Retry/backoff on substation gateway timeouts
- [ ] IEC 60870-5-104 parser for legacy substations

## Owner

Platform team — data-platform@nexdane-energy.com
