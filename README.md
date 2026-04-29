# 🛡️ Spam Detection System using Bidirectional LSTM (Advanced)

🚀 An AI-powered web application that detects whether a message is **Spam or Not Spam** using an advanced **Bidirectional LSTM (BiLSTM)** model trained on real-world and custom datasets.

---

## 📌 Overview

This project leverages **Natural Language Processing (NLP)** and a **Bidirectional LSTM (BiLSTM)** neural network to classify both SMS and email-like messages.

Unlike basic spam detectors, this system can handle:

* Subtle spam
* Professional/phishing-style messages
* Context-based classification

It includes a **trained deep learning model + Flask API + interactive UI** for real-time predictions.

---

## ✨ Features

* 🧠 Bidirectional LSTM (BiLSTM) for better context understanding
* 📊 Trained on advanced + custom datasets
* 🔍 Detects subtle and human-like spam
* 🌐 REST API using Flask
* 🎨 Clean and responsive web interface
* ⚡ Real-time predictions
* 📈 Confidence score output
* 💾 Model persistence (.h5 + tokenizer)

---

## 🧠 Model Improvements

### 🔻 Before

* Basic LSTM
* Keyword-based dataset
* Limited to obvious spam

### 🔺 Now

* Bidirectional LSTM (BiLSTM)
* Advanced + custom dataset
* Context-aware detection
* Improved handling of:

  * Phishing messages
  * Social engineering
  * Indirect promotional spam

---

## 🧠 Model Capability

✔ Detects:

* Keyword-based spam
* Contextual spam
* Subtle promotional messages
* Phishing-like patterns

⚠️ Still challenging:

* Highly personalized scams
* Completely unseen patterns

---

## 🏗️ Project Structure

spam-detector/

│

├── data/

│   ├── raw/

│   └── processed/

│       ├── spam.csv

│       └── advanced_spam.csv

│

├── model/

│   ├── bilstm_model.h5

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

---

## ⚙️ Installation

git clone https://github.com/devams07/spam-detector.git

cd spam-detector

pip install -r requirements.txt

---

## ▶️ How to Run

1. Train the model
   python train.py

2. Run the application
   python app.py

3. Open in browser
   http://127.0.0.1:5000/

---

## 🧪 Example

Input:
"Just checking if you're interested in this opportunity 😊"

Output:
Spam (Confidence: 0.82)

---

## 🧠 Technologies Used

* Python
* TensorFlow / Keras
* Pandas, NumPy
* Flask
* HTML, CSS, JavaScript

---

## 📈 Future Improvements

* Upgrade to Transformer models like BERT
* Improve dataset with real-world phishing data
* Deploy on cloud (AWS / Render)
* Add hybrid detection (ML + rule-based)

---

## 👨‍💻 Author

Deva M S

Aspiring Cybersecurity Engineer

---

## ⭐ Support

If you like this project:

* Star this repo
* Fork it
* Contribute
