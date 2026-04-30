# UniFi Exporter Setup

## Purpose

UniFi metrics are collected using **Unpoller**.

Unpoller connects to the UniFi Network application and exposes UniFi network metrics to Prometheus on port `9130`.

---

## Exporter Used

Unpoller

---

## Metrics Port

9130

---

## Step 1 — Create UniFi Monitoring User

In the UniFi Network application, create a local monitoring user.

Recommended settings:

Username: prometheus  
Role: Read-only or limited admin  

Do not commit the password to GitHub.

---

## Step 2 — Run UniFi Exporter / Unpoller

Replace the password before running:

docker run -d \
  --name unifi-exporter \
  --restart unless-stopped \
  -p 9130:9130 \
  -e UP_UNIFI_DEFAULT_URL="https://10.10.1.1" \
  -e UP_UNIFI_DEFAULT_USER="prometheus" \
  -e UP_UNIFI_DEFAULT_PASS="REPLACE_WITH_YOUR_PASSWORD" \
  -e UP_UNIFI_DEFAULT_VERIFY_SSL="false" \
  -e UP_PROMETHEUS_HTTP_LISTEN="0.0.0.0:9130" \
  ghcr.io/unpoller/unpoller:latest

---

## Step 3 — Verify Container Is Running

docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"

Expected result:

unifi-exporter    0.0.0.0:9130->9130/tcp    Up

---

## Step 4 — Test Metrics Endpoint

curl http://10.10.30.140:9130/metrics

Expected result:

UniFi metrics output

---

## Step 5 — Restart Prometheus

systemctl restart prometheus

---

## Step 6 — Confirm in Prometheus

Open:

http://10.10.30.140:9090/targets

Expected:

unifi-exporter    UP

---

## Prometheus Scrape Config

Add this to prometheus.yml if not present:

- job_name: "unifi-exporter"
  static_configs:
    - targets:
        - "10.10.30.140:9130"
      labels:
        instance: "unifi-exporter"
        service: "unifi"
        role: "network"
        vendor: "unifi"
        site: "ceds-homelab"

---

## Troubleshooting

### Connection Refused

Cause:
Exporter not running or not bound to port 9130.

Fix:

docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"
docker restart unifi-exporter

---

### Authentication Failed

Cause:
Incorrect UniFi credentials.

Fix:
Update credentials and restart container.

---

### Target Still Down in Prometheus

Test exporter:

curl http://10.10.30.140:9130/metrics

Check Prometheus config:

promtool check config /etc/prometheus/prometheus.yml

Restart Prometheus:

systemctl restart prometheus

---

## Security Notes

Never commit:

- UniFi passwords
- API keys
- Cloudflare tokens
- Proxmox credentials
- Grafana credentials

Use placeholders:

REPLACE_WITH_YOUR_PASSWORD

---

## Status

When complete, Prometheus should show:

unifi-exporter    UP

Grafana dashboards can now use UniFi metrics.