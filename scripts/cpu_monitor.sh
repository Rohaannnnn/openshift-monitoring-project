THRESHOLD=80

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d. -f1)

echo "CPU Usage: $CPU%"

if [ "$CPU" -gt "$THRESHOLD" ]
then
    echo "WARNING: High CPU Usage!"
else
    echo "CPU is healthy"
fi
