function predict() {
    let time = document.getElementById("timeInput").value;

    fetch("https://doctor-survey-predictor-production.up.railway.app//predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ time: time })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => { throw new Error(data.message); });
        }
        return response.blob();
    })
    .then(blob => {
        let link = document.createElement("a");
        link.href = window.URL.createObjectURL(blob);
        link.download = "predicted_doctors.csv";
        link.click();
        document.getElementById("message").innerText = "Download ready!";
    })
    .catch(error => {
        document.getElementById("message").innerText = "Error: " + error.message;
    });
}