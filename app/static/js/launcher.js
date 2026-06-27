const launchButton = document.getElementById("launch-button");
const launchStatus = document.getElementById("launch-status");

if (launchButton) {
    launchButton.addEventListener("click", async () => {
        const target = launchButton.dataset.launchTarget;

        launchButton.disabled = true;
        launchStatus.textContent = "Starting...";

        try {
            const response = await fetch(`/api/launch/${target}`, {
                method: "POST"
            });

            const data = await response.json();

            if (data.status === "started") {
                launchStatus.textContent = `${data.app} started successfully.`;
            } else {
                launchStatus.textContent = data.message || "Launch failed.";
            }
        } catch (error) {
            launchStatus.textContent = "Request failed.";
            console.error(error);
        }

        launchButton.disabled = false;
    });
}