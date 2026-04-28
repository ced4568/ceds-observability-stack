# Alerting Strategy

## Purpose

The goal of alerting is not to create noise.

The goal is to identify problems that require action.

---

## Alert Severity Levels

| Severity | Meaning | Example |
|---|---|---|
| Critical | Immediate action required | Node down |
| Warning | Investigate soon | CPU above 85% |
| Info | Awareness only | Service restarted |

---

## Initial Alert Rules

### Critical

- Proxmox node down
- K3s control plane node down
- Core service unavailable
- Storage nearly full
- Cluster quorum issue

### Warning

- High CPU usage
- High memory usage
- High disk usage
- Repeated pod restarts
- Slow service response

---

## Alert Response Process

1. Confirm alert in Grafana
2. Identify affected system
3. Check recent changes
4. Review logs
5. Verify service status
6. Restart or repair if needed
7. Document what happened

---

## Example Incident Notes

```text
Incident:
Service unavailable alert triggered for Nginx Proxy Manager.

Impact:
External service routing may be affected.

Investigation:
Checked host status, container status, and reverse proxy logs.

Resolution:
Restarted affected container and confirmed service recovery.

Follow-up:
Add container-level monitoring and restart alert.