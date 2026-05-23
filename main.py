import psutil
import time

while True:
    print("CPU:", psutil.cpu_percent())
    print("Memory:", psutil.virtual_memory().percent)
    print("Disk:", psutil.disk_usage('/').percent)

    print("-" * 30)

    time.sleep(5)
