# 🚀 Ced’s Observability Stack

![Status](https://img.shields.io/badge/Status-Active%20Development-blue)
![Platform](https://img.shields.io/badge/Platform-Proxmox%20%7C%20K3s-orange)
![Monitoring](https://img.shields.io/badge/Stack-Prometheus%20%7C%20Grafana-red)
![Alerting](https://img.shields.io/badge/Alerting-Alertmanager-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🧠 Executive Summary

**Ced’s Observability Stack** is a production-style monitoring, metrics, and alerting platform built to provide full visibility into a distributed hybrid infrastructure.

It simulates real-world **SRE / Platform Engineering environments**, delivering:

* 📊 Real-time infrastructure monitoring
* ⚙️ Kubernetes observability (12-node K3s cluster)
* 🖥️ Proxmox HA cluster visibility
* 🌐 Service uptime + network health tracking
* 🚨 Alerting pipelines (Alertmanager)
* 📈 Operational dashboards (Grafana)

> 🎯 **Goal:** Demonstrate enterprise-level observability practices across virtualization, Kubernetes, and self-hosted infrastructure.

---

## 🏗️ Environment Overview

### Core Infrastructure

| System                   | Purpose                            |
| ------------------------ | ---------------------------------- |
| 🖥️ Proxmox HA Cluster   | Virtualization & high availability |
| ☸️ K3s Cluster (12-node) | Container orchestration            |
| 💾 TrueNAS               | Storage services                   |
| 🌐 Nginx Proxy Manager   | Reverse proxy & routing            |
| ☁️ Cloudflare            | DNS, tunnels, external protection  |
| 📊 Grafana               | Visualization dashboards           |
| 📡 Prometheus            | Metrics collection                 |
| 🚨 Alertmanager          | Alert routing                      |

---

## 🚀 Quick Start

### Prerequisites

* Linux server or VM
* Python 3 installed
* Prometheus installed
* Grafana installed
* Network access to homelab systems

---

### Run Service Health Check

```bash
python3 scripts/service-health-check.py
```

---

### Run Prometheus

```bash
prometheus --config.file=prometheus/prometheus.yml
```

---

### Access Services

* Prometheus: http://localhost:9090
* Grafana: http://localhost:3000

---

## 📡 Monitored Systems

| Target                  | Example Metrics                      |
| ----------------------- | ------------------------------------ |
| 🖥️ Proxmox Nodes       | CPU, memory, storage, VM + HA status |
| ☸️ K3s Nodes            | Node readiness, resource usage       |
| 📦 Kubernetes Workloads | Pods, deployments, restarts          |
| 🌐 Network Services     | Uptime, latency, TCP checks          |
| 💾 TrueNAS              | Storage + service availability       |
| 🔀 Nginx Proxy Manager  | Reverse proxy health                 |
| 📊 Dashy / NOC          | Dashboard availability               |
| 🎬 Jellyfin             | Media service uptime                 |

---

## 🧩 Architecture

```mermaid
flowchart TD
    A[Proxmox HA Cluster] --> P[Prometheus]
    B[12-Node K3s Cluster] --> P
    C[Node Exporters] --> P
    D[Service Health Checks] --> P
    E[Proxmox Exporter] --> P

    P --> G[Grafana Dashboards]
    P --> AM[Alertmanager]

    AM --> N[Email / Discord / Slack Alerts]
    G --> NOC[Ced's NOC Dashboard]
```

---

## 📸 Dashboards

### Infrastructure Overview

Infrastructure Dashboard

### K3s Cluster Dashboard

K3s Dashboard

### Proxmox HA Dashboard

Proxmox Dashboard

### Service Uptime Dashboard

Services Dashboard

---

## ⚙️ Core Components

### 📡 Prometheus

Collects metrics from:

* Kubernetes endpoints
* Node exporters
* Proxmox exporter
* Custom health scripts
* Static service targets

---

### 📊 Grafana

Provides dashboards for:

* Cluster health
* Resource utilization
* Storage trends
* Service uptime
* Alert visibility

---

### 🚨 Alertmanager

Handles alerting for:

* Node failures
* High CPU / memory
* Service outages
* Pod crash loops
* Proxmox HA issues

---

## 📁 Repo Structure

```
ceds-observability-stack/
├── architecture/
├── prometheus/
├── grafana/
├── exporters/
├── alerting/
├── scripts/
└── docs/
```

---

## 📸 Dashboard Preview

* 🔹 Infrastructure Overview
* 🔹 K3s Cluster Health
* 🔹 Proxmox Cluster Status
* 🔹 Service Uptime Dashboard

---

## 🚀 Deployment (High-Level)

```bash
# Clone repo
git clone https://github.com/ced4568/ceds-observability-stack.git

# Navigate to project
cd ceds-observability-stack

# Deploy Prometheus + exporters
# (Add your actual deployment steps here)

# Access Grafana
http://<your-server-ip>:3000
```

---

## 🎯 Project Roadmap

### Phase 1 — Foundation

* [x] Architecture design
* [x] Repo structure
* [ ] Prometheus base config
* [ ] Grafana datasource

### Phase 2 — Metrics Collection

* [ ] Node exporter
* [ ] K3s metrics
* [ ] Proxmox exporter
* [ ] Uptime checks

### Phase 3 — Dashboards

* [ ] Infrastructure dashboard
* [ ] K3s dashboard
* [ ] Proxmox dashboard
* [ ] Service uptime dashboard

### Phase 4 — Alerting

* [ ] Alertmanager setup
* [ ] Alert rules
* [ ] Notification testing

### Phase 5 — Portfolio Polish

* [ ] Screenshots
* [ ] Architecture diagrams
* [ ] Setup guide
* [ ] Troubleshooting docs

---

## 🧠 Skills Demonstrated

* 📊 Infrastructure Monitoring
* ☸️ Kubernetes Operations
* 📡 Prometheus Configuration
* 📈 Grafana Dashboarding
* 🚨 Alert Engineering
* 🐧 Linux Administration
* 🖥️ Proxmox Virtualization
* ⚙️ SRE Principles
* 🏗️ Platform Engineering

---

## 🔗 Related Projects

| Project           | Purpose                           |
| ----------------- | --------------------------------- |
| Ced’s HomeLab     | Full infrastructure ecosystem     |
| Ced’s NOC         | Visualization + status dashboards |
| Ced’s K3s HomeLab | Kubernetes architecture           |
| Ced’s APRS iGate  | Networking + RF integration       |

---

## 🔗 Integration

This observability stack is part of a larger ecosystem:

* Ced’s HomeLab → Infrastructure layer
* Ced’s Observability Stack → Metrics + monitoring layer
* Ced’s NOC → Visualization and operations layer

Data flows from monitored systems into Prometheus, is visualized in Grafana, and feeds Ced’s NOC dashboard for real-time system visibility.

---

## 🧪 Verification

To verify the system is working correctly:

### Prometheus Targets

* Navigate to: http://localhost:9090/targets
* Confirm all targets show UP

---

### Node Exporter

```bash
curl http://<node-ip>:9100/metrics
```

---

### Service Health Check

```bash
python3 scripts/service-health-check.py
```

---

### Grafana

* Confirm dashboards display real-time metrics
* Verify data source connection to Prometheus
* Check for active alerts

---

### Alert Testing

* Stop a service or node temporarily
* Confirm alert triggers in Prometheus
* Confirm alert appears in Grafana

---

## 📌 Status

🟢 **Active Development**

This project is continuously evolving as part of Ced’s HomeLab ecosystem and professional portfolio.

---

## 💡 Why This Project Matters

This project simulates a production-style observability system used in modern infrastructure environments.

It is designed to demonstrate how distributed systems are monitored, analyzed, and maintained in real-world engineering teams.

Key capabilities include:

* Monitoring a hybrid infrastructure environment (Proxmox HA + K3s cluster)
* Collecting and visualizing system and service metrics
* Tracking service availability and uptime
* Detecting infrastructure and application-level failures
* Supporting alert-driven operations
* Integrating with a centralized NOC dashboard

This project represents a shift from running infrastructure to actively operating and maintaining it using observability principles aligned with SRE and platform engineering practices.

---

## 🧠 Future Improvements

* Loki log aggregation
* Tempo tracing
* Cloudflare Access log ingestion
* Automated remediation (self-healing infrastructure)
* Grafana public demo dashboard
* GitOps-based deployment (Argo CD / Flux)
* Multi-cluster Kubernetes monitoring

---

## Current Deployment Status

Ced’s Observability Stack is now actively collecting live metrics from Ced’s HomeLab.

Current working components:

- Prometheus metrics collection
- Grafana dashboard visualization
- Proxmox node exporter monitoring
- K3s node exporter monitoring
- kube-state-metrics for Kubernetes object state
- Windows exporter for PrimeStation
- Blackbox HTTP/TCP endpoint probing
- TrueNAS Graphite exporter
- UniFi exporter using Unpoller

Some Grafana panels are being refined as dashboard queries are aligned with available Prometheus metrics.

---

## Production Dashboards

| Dashboard | Purpose |
|---|---|
| Ced's NOC - Production Command Center v3 | Stable executive NOC view for service availability, K3s, Proxmox, PrimeStation, and latency |
| Ced's NOC - Deep Observability v3 | Full drill-down dashboard for Proxmox, K3s, services, UniFi, PrimeStation, and alerts |
| Ced's K3s Elite Observability v1 | Dedicated K3s dashboard using node-exporter and kube-state-metrics |

---

## Phase 3 Live Metrics Milestone

- [x] Prometheus running
- [x] Grafana connected to Prometheus
- [x] Proxmox node exporters reporting
- [x] K3s node exporters reporting
- [x] kube-state-metrics installed and reporting
- [x] Windows exporter reporting
- [x] Blackbox Exporter repaired
- [x] Internal HTTP probes working
- [x] UniFi exporter installed
- [x] Grafana dashboards receiving live data
