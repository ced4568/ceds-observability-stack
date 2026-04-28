```markdown
# K3s Metrics

## Purpose

K3s metrics provide visibility into the Kubernetes cluster.

This project monitors:

- Node readiness
- Pod health
- Deployment status
- Restart counts
- CPU usage
- Memory usage
- Control plane availability

---

## Recommended Components

| Component | Purpose |
|---|---|
| Metrics Server | Basic Kubernetes resource metrics |
| Kube-State-Metrics | Kubernetes object state |
| Node Exporter | Linux node metrics |
| Prometheus | Metrics collection |
| Grafana | Visualization |

---

## Useful Commands

### View Nodes

```bash
kubectl get nodes -o wide