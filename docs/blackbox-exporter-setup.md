# Blackbox Exporter Setup

## Purpose

Blackbox Exporter is used to monitor endpoint availability from Prometheus.

---

## Config Location

/opt/blackbox/blackbox.yml

---

## Setup

```bash
sudo mkdir -p /opt/blackbox
sudo nano /opt/blackbox/blackbox.yml

## Config File

Create or edit:

/opt/blackbox/blackbox.yml

Paste:

    modules:
      http_2xx:
        prober: http
        timeout: 10s
        http:
          method: GET
          preferred_ip_protocol: ip4

      http_2xx_insecure:
        prober: http
        timeout: 10s
        http:
          method: GET
          preferred_ip_protocol: ip4
          tls_config:
            insecure_skip_verify: true

      tcp_connect:
        prober: tcp
        timeout: 5s

      icmp:
        prober: icmp
        timeout: 5s

---

## Remove Old Containers

Run:

    docker rm -f blackbox
    docker rm -f blackbox-exporter

---

## Start Exporter

Run:

    docker run -d \
      --name blackbox-exporter \
      --restart unless-stopped \
      -p 9115:9115 \
      -v /opt/blackbox/blackbox.yml:/config/blackbox.yml:ro \
      prom/blackbox-exporter:latest \
      --config.file=/config/blackbox.yml

---

## Test

Run:

    curl "http://10.10.30.140:9115/probe?target=http://10.10.30.68:3000&module=http_2xx_insecure"

Expected output should include:

    probe_success 1

---

## Restart Prometheus

Run:

    systemctl restart prometheus

---

## Verify in Prometheus

Open:

    http://10.10.30.140:9090/targets

You should now see:

    blackbox-http-internal    UP

---

## Troubleshooting

### Unknown module "http_2xx_insecure"

Cause:
Blackbox Exporter is running with an old or incorrect config.

Fix:
Restart the container after verifying the config file is mounted correctly.

---

### Port already allocated

Cause:
Another container is using port 9115.

Fix:

    docker ps --format "table {{.Names}}\t{{.Ports}}"
    docker rm -f <container-name>