# P2P Encrypted File Sync with CRDT — Dropbox without central server

Sync directly between your devices, E2E encrypted, CRDT conflict-free merging for simultaneous edits to same file/folder. Small feature list, huge implementation: distributed sync + encryption + CRDT.

## Architecture
- **Backend:** Python (CRDT, sync) + Django, PostgreSQL (sqlite fallback)
- **Frontend:** React 18 + Vite
- **Apps:** vault (keys), sync (p2p), crdt (files/folders), encryption, network, storage

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t p2p-sync .
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
```

## Tests
```bash
pytest -q
```

## Features
- **E2E:** X25519 + AES-GCM, zero-knowledge, device pairing via QR
- **CRDT:** LWW-Register per file, OR-Set for folder, vector clocks
- **Sync:** direct WebRTC/DataChannel, hole punching, relay fallback
- **Conflict:** simultaneous edits to same file → CRDT merge, no central server

## License
Proprietary
