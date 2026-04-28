---

# 16. docs/troubleshooting.md

```markdown
# Troubleshooting Guide

## Prometheus Target Down

### Symptoms

Prometheus shows target as DOWN.

### Checks

```bash
ping TARGET_IP
curl http://TARGET_IP:9100/metrics
systemctl status prometheus-node-exporter