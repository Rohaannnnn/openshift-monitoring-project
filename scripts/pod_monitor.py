pods = {
    "frontend": "Running",
    "backend": "Running",
    "database": "CrashLoopBackOff"
}

for pod, status in pods.items():
    print(f"{pod}: {status}")

    if status != "Running":
        print(f"ALERT: {pod} failed")
