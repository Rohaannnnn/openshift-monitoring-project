# Runbook: Node Pressure

## Trigger
`NodeMemoryPressure` or `NodeDiskPressure` indicates sustained pressure reported by a node.

## Investigation
```bash
oc get nodes
oc describe node <node>
oc adm top nodes
oc get pods -A -o wide | grep <node>
oc get events -A --sort-by=.lastTimestamp
```

Check allocatable resources, filesystem pressure, eviction signals, workload placement, and recent node changes.

## Resolution
Drain or remediate the node only according to the cluster's operational policy. Remove the underlying resource pressure, restore node health, and verify the condition clears before returning the node to normal service.
