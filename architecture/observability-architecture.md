```markdown
# Observability Architecture

## Purpose

This document explains the architecture of Ced’s Observability Stack.

The observability stack collects, stores, and visualizes metrics from Ced’s HomeLab infrastructure.

---

## High-Level Design

```mermaid
flowchart LR
    subgraph Infrastructure
        PVE[Proxmox HA Cluster]
        K3S[12-Node K3s Cluster]
        TN[TrueNAS]
        NPM[Nginx Proxy Manager]
        SVC[Homelab Services]
    end

    subgraph Metrics
        NE[Node Exporter]
        PME[Proxmox Exporter]
        KSM[Kube-State-Metrics]
        HC[Health Check Scripts]
    end

    subgraph Observability
        PROM[Prometheus]
        GRAF[Grafana]
        ALERT[Alertmanager]
    end

    PVE --> PME
    K3S --> KSM
    SVC --> HC
    TN --> HC
    NPM --> HC

    PME --> PROM
    KSM --> PROM
    NE --> PROM
    HC --> PROM

    PROM --> GRAF
    PROM --> ALERT

    GRAF --> NOC[Ced's NOC]
