// Spam Feature Descriptions
const featureDescriptions = {
    "has_url": "Contains URLs or web links",
    "repeated_punct": "Excessive punctuation (!!! ???)",
    "money_symbols": "Money/price references",
    "excessive_caps": "EXCESSIVE UPPERCASE TEXT",
    "numbers": "Multiple numbers/codes",
    "suspicious_words": "Urgency or action words",
    "business_scam": "Business/opportunity language",
    "social_engineering": "Social manipulation tactics",
    "phishing": "Account/verification requests",
    "urgency_pressure": "Time pressure/urgency tactics"
};

async function checkSpam() {
    const message = document.getElementById("message").value;
    const errorMsg = document.getElementById("errorMsg");
    const resultSection = document.getElementById("resultSection");

    // Validation
    if (!message.trim()) {
        errorMsg.textContent = "❌ Please enter a message to analyze";
        errorMsg.classList.add("show");
        return;
    }

    errorMsg.classList.remove("show");
    resultSection.classList.add("active");

    // Show loading state
    const resultTitle = document.getElementById("resultTitle");
    const resultDescription = document.getElementById("resultDescription");
    const resultIcon = document.getElementById("resultIcon");

    resultTitle.textContent = "Analyzing...";
    resultDescription.textContent = "Processing your message with AI";
    resultIcon.innerHTML = '<div class="spinner"></div>';

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();
        displayResult(data.result);
    } catch (error) {
        console.error("Error:", error);
        resultTitle.textContent = "Error";
        resultDescription.textContent = "Failed to analyze message. Please try again.";
        resultIcon.innerHTML = '<i class="fas fa-exclamation-circle"></i>';
    }
}

function displayResult(result) {
    const resultTitle = document.getElementById("resultTitle");
    const resultDescription = document.getElementById("resultDescription");
    const resultIcon = document.getElementById("resultIcon");
    const confidenceFill = document.getElementById("confidenceFill");
    const confidenceValue = document.getElementById("confidenceValue");
    const featuresGrid = document.getElementById("featuresGrid");

    const isSpam = result.label === "Spam";
    const confidence = Math.round(result.confidence * 100);

    // Update title and icon
    if (isSpam) {
        resultTitle.textContent = "🚨 Spam Detected";
        resultDescription.textContent = "This message appears to be spam based on multiple indicators";
        resultIcon.innerHTML = '<i class="fas fa-exclamation-triangle"></i>';
        resultIcon.className = "result-icon spam";
        confidenceFill.className = "bar-fill spam";
    } else {
        resultTitle.textContent = "✓ Safe Message";
        resultDescription.textContent = "This message appears to be legitimate";
        resultIcon.innerHTML = '<i class="fas fa-check-circle"></i>';
        resultIcon.className = "result-icon safe";
        confidenceFill.className = "bar-fill safe";
    }

    // Animate confidence bar
    setTimeout(() => {
        confidenceFill.style.width = confidence + "%";
    }, 100);

    confidenceValue.textContent = confidence + "%";

    // Display detected features
    const detectedFeatures = Object.entries(result.spam_features)
        .filter(([_, value]) => value)
        .map(([key, _]) => key);

    if (detectedFeatures.length > 0) {
        featuresGrid.innerHTML = detectedFeatures
            .map(feature => `
                <div class="feature-badge active" title="${featureDescriptions[feature] || feature}">
                    ${formatFeatureName(feature)}
                </div>
            `)
            .join("");
    } else {
        featuresGrid.innerHTML = '<div class="feature-badge">No suspicious patterns</div>';
    }
}

function formatFeatureName(feature) {
    return feature
        .replace(/_/g, " ")
        .split(" ")
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ");
}

function clearInput() {
    document.getElementById("message").value = "";
    document.getElementById("resultSection").classList.remove("active");
    document.getElementById("errorMsg").classList.remove("show");
    document.getElementById("message").focus();
}

// Allow Enter key to submit (Ctrl+Enter)
document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.getElementById("message");
    textarea.addEventListener("keydown", function(event) {
        if (event.ctrlKey && event.key === "Enter") {
            checkSpam();
        }
    });
});