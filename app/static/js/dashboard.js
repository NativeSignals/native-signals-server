async function updateStatus() {
    try {
        const response = await fetch("/api/status");
        const data = await response.json();

        setStatus("status-xr18", data.xr18);
        setStatus("status-boss_head_1", data.boss_head_1);
        setStatus("status-boss_head_2", data.boss_head_2);
        setStatus("status-prompter", data.prompter);
        setStatus("status-recording", data.recording);
        setStatus("status-desktop", data.desktop);
    } catch (error) {
        console.error("Status update failed:", error);
    }
}

function setStatus(id, status) {
    const element = document.getElementById(id);

    if (!element) {
        return;
    }

    element.classList.remove("online", "offline", "standby");
    element.classList.add(status);
}

updateStatus();
setInterval(updateStatus, 2000);