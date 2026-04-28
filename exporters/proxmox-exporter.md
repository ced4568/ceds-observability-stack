
```markdown
# Proxmox Exporter

## Purpose

The Proxmox exporter exposes Proxmox metrics to Prometheus.

It can be used to monitor:

- Proxmox node health
- VM and container status
- Storage usage
- Cluster resources
- CPU and memory usage

---

## Recommended Metrics

| Metric Area | Purpose |
|---|---|
| Node Status | Verify Proxmox nodes are online |
| VM Status | Track virtual machines |
| Storage | Monitor pool and disk usage |
| CPU | Detect high compute usage |
| Memory | Detect memory pressure |
| Cluster | Monitor HA and quorum health |

---

## Security Notes

Do not commit real Proxmox tokens, usernames, passwords, or secrets to GitHub.

Use environment variables or a local `.env` file.

The `.env` file should be included in `.gitignore`.

---

## Example Environment Variables

```bash
PROXMOX_HOST=10.10.30.250
PROXMOX_PORT=8006
PROXMOX_USER=monitoring@pve
PROXMOX_TOKEN_NAME=prometheus
PROXMOX_TOKEN_VALUE=REPLACE_ME