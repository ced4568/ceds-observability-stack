#!/usr/bin/env python3

import json
import socket
import time
from datetime import datetime, timezone

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
    except OSError:
        return False, None


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def main():
    results = []

    for service in SERVICES:
        online, latency = check_tcp(service["host"], service["port"])

        results.append(
            {
                "name": service["name"],
                "host": service["host"],
                "port": service["port"],
                "online": online,
                "latency_ms": latency,
                "checked_at": utc_now(),
            }
        )

    summary = {
        "checked_at": utc_now(),
        "total_services": len(results),
        "online_services": sum(1 for result in results if result["online"]),
        "offline_services": sum(1 for result in results if not result["online"]),
        "services": results,
    }

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()