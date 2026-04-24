async function checkSpam() {
    const message = document.getElementById("message").value;
    const resultDiv = document.getElementById("result");

    if (!message.trim()) {
        resultDiv.innerHTML = "Enter a message";
        return;
    }

    resultDiv.innerHTML = "<span class='loading'>Analyzing...</span>";

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    if (data.result === "Spam") {
        resultDiv.innerHTML = "<span class='spam'>Spam Detected 🚨</span>";
    } else {
        resultDiv.innerHTML = "<span class='safe'>Safe Message</span>";
    }
}