# OpenShift Cluster & User Workload Monitoring

This repository manages custom monitoring assets, alerting rules, and observability configurations for OpenShift Container Platform (OCP) using the native CoreOS Prometheus Operator and User Workload Monitoring (UWM) framework.

---

## Architecture Overview

OpenShift uses two isolated monitoring stacks managed by the cluster-monitoring-operator:
1. Cluster Monitoring: Monitors core OCP components (Control Plane, Nodes, Kubelet, OpenShift API).
2. User Workload Monitoring (UWM): Dedicated Prometheus stack deployed in openshift-user-workload-monitoring for monitoring custom user applications and namespaces.

---

## Repository Structure
.
├── cluster-config/              # OpenShift Cluster Monitoring ConfigMaps
│   ├── user-workload-monitoring.yaml # Enables UWM via cluster-monitoring-config
│   └── retention-config.yaml    # Metrics retention & storage persistence
├── manifests/
│   ├── service-monitors/        # ServiceMonitor definitions for custom apps
│   ├── pod-monitors/            # PodMonitor definitions (bypassing Services)
│   └── prometheus-rules/        # Custom Alertmanager & Recording rules
├── dashboards/
│   └── grafana-dashboards/      # Custom Grafana dashboard JSON models
└── docs/                        # Architecture diagrams & OCP CLI notes
---

## Quickstart & Deployment

### 1. Enable User Workload Monitoring on OpenShift
Ensure UWM is enabled on your OCP cluster by applying the cluster-monitoring-config ConfigMap:
bash
oc apply -f cluster-config/user-workload-monitoring.yaml

### 2. Verify Monitoring Pods are Running

bash
oc get pods -n openshift-user-workload-monitoring
### 3. Deploy App ServiceMonitors & Alert Rules
oc apply -f manifests/service-monitors/


oc apply -f manifests/prometheus-rules/

---

## OpenShift Role-Based Access Control (RBAC)

To allow team members to view metrics without giving them cluster-admin rights:
- monitoring-rules-view: Grants permission to view Prometheus alert rules.
- monitoring-edit: Grants permission to create ServiceMonitor and PodMonitor CRDs inside a namespace.


oc adm policy add-role-to-user monitoring-edit  -n


