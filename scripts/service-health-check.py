---

# 14. scripts/service-health-check.py

```python
#!/usr/bin/env python3

import socket
import time
import json
from datetime import datetime

SERVICES = [
    {"name": "Proxmox", "host": "10.10.30.250", "port": 8006},
    {"name": "TrueNAS", "host": "10.10.30.143", "port": 80},
    {"name": "Nginx Proxy Manager", "host": "10.10.30.210", "port": 81},
    {"name": "Dashy", "host": "10.10.30.61", "port": 4000},
    {"name": "Jellyfin", "host": "10.10.30.143", "port": 30013},
]

def check_tcp(host, port, timeout=3):
    start = time.time()

    try:
        with socket.create_connection((host, port), timeout=timeout):
            latency_ms = round((time.time() - start) * 1000, 2)
            return True, latency_ms
    except Exception:
        return False, None

def main():
    results = []

    for service in SERVICES:
        online, latency = check_tcp(service["host"], service["port"])

        results.append({
            "name": service["name"],
            "host": service["host"],
            "port": service["port"],
            "online": online,
            "latency_ms": latency,
            "checked_at": datetime.utcnow().isoformat() + "Z"
        })

    summary = {
        "checked_at": datetime.utcnow().isoformat() + "Z",
        "total_services": len(results),
        "online_services": sum(1 for r in results if r["online"]),
        "offline_services": sum(1 for r in results if not r["online"]),
        "services": results
    }

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()