import socket
from datetime import datetime

import psutil
import requests


LHM_URL = "http://127.0.0.1:8085/data.json"


def find_sensor(node, sensor_id):
    if node.get("SensorId") == sensor_id:
        return node.get("Value")

    for child in node.get("Children", []):
        result = find_sensor(child, sensor_id)
        if result is not None:
            return result

    return None


def get_cpu_temperature():
    try:
        response = requests.get(LHM_URL, timeout=1)
        response.raise_for_status()
        data = response.json()

        return find_sensor(data, "/amdcpu/0/temperature/2")
    except Exception:
        return None


def get_system_status():
    boot = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot

    hours = int(uptime.total_seconds() // 3600)
    minutes = int((uptime.total_seconds() % 3600) // 60)

    temperature = get_cpu_temperature()

    return {
        "cpu": psutil.cpu_percent(interval=0.2),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("C:\\").percent,
        "ip": socket.gethostbyname(socket.gethostname()),
        "uptime": f"{hours}h {minutes}m",
        "temperature": temperature
    }