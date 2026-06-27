async function updateSystemStatus() {
    try {
        const response = await fetch("/api/system");
        const data = await response.json();

        document.getElementById("cpu").textContent =
            data.cpu + " %";

        document.getElementById("ram").textContent =
            data.ram + " %";

        document.getElementById("disk").textContent =
            data.disk + " %";

        document.getElementById("ip").textContent =
            data.ip;

        document.getElementById("uptime").textContent =
            data.uptime;

        if (data.temperature !== null) {
            document.getElementById("temperature").textContent =
                data.temperature;
        }

    } catch (error) {
        console.error(error);
    }
}

updateSystemStatus();
setInterval(updateSystemStatus, 2000);