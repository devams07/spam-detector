import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils.preprocess import clean_text

model = load_model("model/lstm_model.h5")

with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

def predict(text):
    text = clean_text(text)
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=60)

    pred = model.predict(padded)[0][0]
    return "Spam" if pred > 0.5 else "Not Spam"