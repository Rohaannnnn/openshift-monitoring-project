# Troubleshooting Workflow

Use the same investigation loop for every incident:

## 1. Problem
Start from the alert, affected namespace/pod/node, severity, and start time.

## 2. Monitoring
Confirm the signal in Prometheus/OpenShift monitoring and determine whether it is isolated or systemic.

## 3. Alert
Read the alert expression, duration, labels, annotations, and linked runbook before changing anything.

## 4. Investigation
Correlate metrics with:

```bash
oc get pods -A -o wide
oc describe pod <pod> -n <namespace>
oc get events -n <namespace> --sort-by=.lastTimestamp
oc logs <pod> -n <namespace> --tail=200
oc adm top pods -A
oc adm top nodes
```

For a rollout-related incident:

```bash
oc rollout history deployment/<deployment> -n <namespace>
oc rollout status deployment/<deployment> -n <namespace>
```

## 5. Resolution
Apply the smallest safe remediation, document what changed, and avoid deleting/restarting resources blindly.

## 6. Verification
Confirm the metric returns to baseline, the alert clears, the workload becomes healthy, and no related alerts remain active.

## Common failure modes

| Symptom | First checks | Likely causes |
|---|---|---|
| High CPU | `oc adm top pods`, pod limits | traffic spike, inefficient code, undersized requests |
| High memory | working set, limits, OOM events | leak, cache growth, undersized limit |
| CrashLoopBackOff | `oc logs --previous`, `describe` | bad config, dependency failure, probe failure |
| Not Ready | readiness probe, events | dependency, image, mount, probe |
| Node pressure | `oc describe node`, `oc adm top nodes` | disk exhaustion, memory pressure, scheduling imbalance |
