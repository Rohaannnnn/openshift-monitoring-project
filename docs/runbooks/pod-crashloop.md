# Runbook: Pod CrashLoop

## Trigger
`PodCrashLooping` fires after at least three container restarts in 15 minutes.

## Investigation
```bash
oc get pod <pod> -n <namespace> -o wide
oc describe pod <pod> -n <namespace>
oc logs <pod> -n <namespace> --previous
oc get events -n <namespace> --sort-by=.lastTimestamp
```

Inspect the termination reason, exit code, probes, image/configuration changes, secrets, and resource limits.

## Resolution
Fix the failed startup dependency, configuration, probe, image, or resource constraint. Redeploy if required and verify restart counts stop increasing.
