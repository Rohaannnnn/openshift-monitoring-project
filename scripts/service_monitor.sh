SERVICE="ssh"

if systemctl is-active --quiet $SERVICE
then
    echo "$SERVICE is running"
else
    echo "$SERVICE is down"
fi
