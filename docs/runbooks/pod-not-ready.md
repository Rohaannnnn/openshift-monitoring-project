# Runbook: Pod Not Ready

## Trigger
`PodNotReady` fires when a pod remains unready for 10 minutes.

## Investigation
```bash
oc get pod <pod> -n <namespace>
oc describe pod <pod> -n <namespace>
oc get endpoints -n <namespace>
oc get events -n <namespace> --sort-by=.lastTimestamp
```

Inspect readiness probes, scheduling state, image pulls, mounts, dependencies, and recent rollout history.

## Resolution
Correct the readiness condition or dependency, then verify the pod becomes Ready and service endpoints recover.
