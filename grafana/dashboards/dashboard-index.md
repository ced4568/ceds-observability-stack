# Grafana Dashboard Index

## Planned Dashboards

### 1. Ced’s Infrastructure Overview

Purpose:

- High-level health summary
- Online/offline systems
- Active alerts
- CPU and memory overview
- Service uptime

Panels:

- Total monitored systems
- Systems online
- Systems offline
- Active alerts
- Average CPU usage
- Average memory usage

---

### 2. Proxmox HA Dashboard

Purpose:

- Monitor Proxmox cluster health

Panels:

- Proxmox node status
- HA status
- VM status
- CPU usage by node
- Memory usage by node
- Storage usage
- Cluster quorum

---

### 3. K3s Cluster Dashboard

Purpose:

- Monitor Kubernetes cluster health

Panels:

- Node readiness
- Pod status
- Deployment status
- Restart counts
- CPU usage
- Memory usage
- Control plane status

---

### 4. Homelab Services Dashboard

Purpose:

- Monitor core services

Services:

- Proxmox
- TrueNAS
- Nginx Proxy Manager
- Dashy
- Jellyfin
- NOC Dashboard

Panels:

- Service status
- Response time
- Uptime percentage
- Failed checks

---

### 5. Alert Operations Dashboard

Purpose:

- Track alert history and current alert state

Panels:

- Active alerts
- Critical alerts
- Warning alerts
- Alert frequency
- Alert source