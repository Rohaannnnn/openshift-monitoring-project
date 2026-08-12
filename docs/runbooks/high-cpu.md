# Runbook: High CPU

## Trigger
`WorkloadHighCPU` fires when a pod sustains more than 0.8 CPU cores for 10 minutes.

## Investigation
```bash
oc get pods -A -o wide
oc top pods -A
oc describe pod <pod> -n <namespace>
oc get events -n <namespace> --sort-by=.lastTimestamp
oc logs <pod> -n <namespace> --tail=200
```

## Checks
- Confirm whether the workload is expected to scale under load.
- Compare current CPU with requests/limits.
- Look for recent deployments or configuration changes.
- Check whether one container is responsible for most usage.

## Resolution
Scale replicas, tune resource requests/limits, or fix the application workload as appropriate. Verify CPU returns to normal and the alert clears.
