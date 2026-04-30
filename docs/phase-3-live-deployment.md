# Phase 3 — Live Deployment Notes

## Overview

Phase 3 focused on moving Ced’s Observability Stack from documentation into a working live monitoring environment.

The goal was to verify that Prometheus could collect real metrics from Ced’s HomeLab infrastructure and that Grafana could visualize those metrics through live dashboards.

---

## Environment

| System | Purpose |
|---|---|
| Prometheus CT | Metrics collection |
| Grafana CT | Dashboard visualization |
| Blackbox Exporter | Service availability checks |
| Node Exporter | Host-level metrics |
| Unpoller / UniFi Exporter | UniFi network metrics |
| TrueNAS Graphite Exporter | TrueNAS metrics |
| Proxmox HA Cluster | Virtualization platform |
| 12-node K3s Cluster | Kubernetes environment |

---

## Completed Work

- Verified Prometheus target health
- Repaired Blackbox Exporter configuration
- Added custom Blackbox modules
- Fixed HTTP probing for internal services
- Verified Proxmox node exporter targets
- Verified K3s node exporter targets
- Installed UniFi exporter using Unpoller
- Verified UniFi metrics on port 9130
- Confirmed all Prometheus targets are UP
- Verified Grafana dashboards are receiving live data

---

## Services Confirmed Working

| Component | Status |
|---|---|
| Prometheus | UP |
| Blackbox Exporter | UP |
| Proxmox Node Exporters | UP |
| K3s Node Exporters | UP |
| Windows Exporter | UP |
| TrueNAS Graphite Exporter | UP |
| UniFi Exporter / Unpoller | UP |
| Grafana Dashboards | Partially complete and receiving live data |

---

## Key Outcome

At the end of this phase, Ced’s Observability Stack successfully collected metrics from multiple platforms across the homelab environment.

This moved the project from a documentation-only repo into a real operating observability system.