import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def clean_text(text):
    """Enhanced preprocessing that preserves spam indicators"""
    text = text.lower()
    
    # Preserve important patterns:
    # 1. Replace URLs with a placeholder to preserve presence
    text = re.sub(r'http[s]?://\S+|www\.\S+', ' URL ', text)
    
    # 2. Preserve repeated punctuation (!!!, ???, etc.) as spam signal
    text = re.sub(r'([!?]){2,}', r'\1 REPEATED_PUNCT ', text)
    
    # 3. Preserve money/price signals ($, £, €)
    text = re.sub(r'[\$£€]', ' MONEY ', text)
    
    # 4. Preserve numbers patterns (common in spam)
    text = re.sub(r'\d+', ' NUM ', text)
    
    # 5. Keep common spam words with special chars (e.g., c0ngrats, cl!ck)
    # by replacing problematic chars with space
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    
    # 6. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def tokenize(texts, max_words=8000, max_len=100):
    tokenizer = Tokenizer(num_words=max_words)
    tokenizer.fit_on_texts(texts)

    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, maxlen=max_len)

    return tokenizer, padded