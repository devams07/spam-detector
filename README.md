# 🛡️ Spam Detection System using LSTM

🚀 A modern AI-powered web application that detects whether a message is **Spam or Not Spam** using a deep learning model (LSTM).

---

## 📌 Overview

This project uses **Natural Language Processing (NLP)** and a **Bidirectional Long Short-Term Memory (LSTM)** neural network to classify SMS/email messages.
It includes a **trained ML model + Flask API + interactive UI** for real-time predictions.

---

## ✨ Features

* 🧠 Deep Learning model (LSTM)
* 📊 Trained on real-world spam dataset
* 🌐 REST API using Flask
* 🎨 Clean & modern web UI
* ⚡ Real-time spam prediction
* 💾 Model persistence (`.h5` + tokenizer)

---

## 🧠 Model Note (Important)

⚠️ This model is **trained on a basic spam dataset**, which mainly contains common spam patterns like:

* “Win money”
* “Free offer”
* “Click now”

👉 Because of this, the model may **not detect advanced or human-like spam messages**, such as:

* Social engineering attacks
* Personalized phishing messages
* Obfuscated text (e.g., `C0ngr@ts`)

💡 **To improve accuracy:**

* Train the model with your **own custom dataset**
* Include **real-world phishing & modern spam examples**
* Combine **ML + rule-based detection (links, keywords, urgency)**

---

## 🏗️ Project Structure

```
spam-detector/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── spam.csv
│
├── model/
│   ├── lstm_model.h5
│   └── tokenizer.pkl
│
├── utils/
│   ├── preprocess.py
│   └── dataset.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── script.js
│
├── train.py
├── predict.py
├── app.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/spam-detector.git
cd spam-detector
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 1️⃣ Train the model

```bash
python train.py
```

### 2️⃣ Run the application

```bash
python app.py
```

### 3️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Usage

### ✅ Input:

```
"Congratulations! You won a free prize"
```

### 🚨 Output:

```
Spam
```

---

## 🧠 Technologies Used

* 🐍 Python
* 🔬 TensorFlow / Keras
* 📊 Pandas, NumPy
* 🌐 Flask
* 🎨 HTML, CSS, JavaScript

---

## 📈 Future Improvements

* 🔥 Upgrade to BERT (Transformer model)
* 📊 Show prediction confidence (%)
* 📱 Mobile responsive UI
* ☁️ Cloud deployment (Render / AWS)
* 🧠 Improve dataset with real-world phishing samples

---

## 👨‍💻 Author

**Deva M S**
💼 Aspiring Cybersecurity Engineer

---

## ⭐ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 🛠️ Contribute

---
