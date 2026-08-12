# Runbook: High Memory

## Trigger
`WorkloadHighMemory` fires when a pod exceeds 1 GiB of working-set memory for 10 minutes.

## Investigation
```bash
oc top pod <pod> -n <namespace>
oc describe pod <pod> -n <namespace>
oc get events -n <namespace> --sort-by=.lastTimestamp
```

Check container limits, recent releases, memory growth, and whether the pod is approaching an OOMKill.

## Resolution
Correct the application leak or workload behavior, or adjust resources based on measured requirements. Confirm memory stabilizes and the alert clears.
