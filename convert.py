import pandas as pd
import os

input_path = "data/raw/SMSSpamCollection"
output_path = "data/processed/spam.csv"

os.makedirs("data/processed", exist_ok=True)

data = []
with open(input_path, encoding="utf-8") as f:
    for line in f:
        label, text = line.strip().split("\t", 1)
        data.append([label, text])

df = pd.DataFrame(data, columns=["label", "text"])
df.to_csv(output_path, index=False)

print("Done")