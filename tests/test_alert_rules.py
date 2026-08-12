from pathlib import Path

import yaml


RULE_FILE = Path(__file__).parents[1] / "manifests" / "prometheus-rules" / "openshift-workload-alerts.yaml"
EXPECTED_ALERTS = {
    "WorkloadHighCPU",
    "WorkloadHighMemory",
    "PodCrashLooping",
    "PodNotReady",
    "NodeMemoryPressure",
    "NodeDiskPressure",
}


def load_rules():
    with RULE_FILE.open() as handle:
        return yaml.safe_load(handle)


def test_prometheus_rule_shape():
    document = load_rules()
    assert document["apiVersion"] == "monitoring.coreos.com/v1"
    assert document["kind"] == "PrometheusRule"
    assert document["spec"]["groups"]


def test_expected_alerts_are_present():
    document = load_rules()
    alerts = {
        rule["alert"]
        for group in document["spec"]["groups"]
        for rule in group["rules"]
    }
    assert EXPECTED_ALERTS <= alerts


def test_alerts_have_runbooks_and_severity():
    document = load_rules()
    for group in document["spec"]["groups"]:
        for rule in group["rules"]:
            assert rule["labels"]["severity"] in {"warning", "critical"}
            assert rule["annotations"]["runbook"].startswith("docs/runbooks/")
