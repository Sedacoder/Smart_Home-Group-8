async function updateDashboard() {
    const response = await fetch("/api/status");
    const data = await response.json();

    document.getElementById("bin-level").textContent =
        `Bin Level: ${data.bin.bin_level}%`;
    document.getElementById("bin-notification").textContent =
        data.bin.notification;
}

// Update immediately, then every 5 seconds
updateDashboard();
setInterval(updateDashboard, 5000);
