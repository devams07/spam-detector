import pandas as pd
from sklearn.model_selection import train_test_split
from utils.preprocess import clean_text, tokenize

def load_data(path):
    df = pd.read_csv(path, encoding='latin-1')

    # Take only first two columns (label + text)
    df = df.iloc[:, :2]
    df.columns = ['label', 'text']

    df['text'] = df['text'].apply(clean_text)
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    tokenizer, X = tokenize(df['text'])
    y = df['label']

    return train_test_split(X, y, test_size=0.2, random_state=42), tokenizer