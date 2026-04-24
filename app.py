from flask import Flask, request, jsonify, render_template
from predict import predict

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def detect_spam():
    data = request.json
    message = data.get("message")

    result = predict(message)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)