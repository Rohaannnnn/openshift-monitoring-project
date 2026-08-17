# Evidence Screenshots

Capture screenshots from a real OpenShift lab/cluster and place them in this directory.

Recommended evidence:

1. OpenShift monitoring dashboard showing workload CPU/memory.
2. A fired `WorkloadHighCPU` or `WorkloadHighMemory` alert.
3. A `CrashLoopBackOff` investigation showing `oc describe` and previous logs.
4. A node health/pressure view.
5. GitHub Actions showing the CI checks passing.

Do not use fabricated production screenshots. The evidence should correspond to an actual run of the manifests and runbooks in this repository.
