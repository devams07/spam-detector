import pickle
from utils.dataset import load_data
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional

(X_train, X_test, y_train, y_test), tokenizer = load_data("data/processed/spam.csv")

model = Sequential()

model.add(Embedding(8000, 128, input_length=100))

# 🔥 Bidirectional LSTM
model.add(Bidirectional(LSTM(128, return_sequences=False)))

model.add(Dropout(0.5))

model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

model.save("model/bilstm_model.h5")

with open("model/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("Training Done")