import pickle
import re
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils.preprocess import clean_text

# Load model
model = load_model("model/bilstm_model.h5")   # ✅ updated name

# Load tokenizer
with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 100   # ⚠️ increased to capture longer spam patterns

def detect_spam_features(raw_text):
    """Detect advanced spam features including social engineering patterns"""
    features = {
        "has_url": bool(re.search(r'http[s]?://\S+|www\.\S+', raw_text, re.IGNORECASE)),
        "repeated_punct": bool(re.search(r'([!?]){2,}|(\\.){2,}', raw_text)),
        "money_symbols": bool(re.search(r'[\$£€₹]|\bfree\b|\bwin\b|\bprize\b|\bcomplimentary\b', raw_text, re.IGNORECASE)),
        "excessive_caps": len(re.findall(r'[A-Z]', raw_text)) > len(raw_text) * 0.3 if raw_text else False,
        "numbers": bool(re.search(r'\d{3,}', raw_text)),  # Multiple numbers
        "suspicious_words": bool(re.search(r'\b(click|verify|confirm|urgent|act|limited|now)\b', raw_text, re.IGNORECASE)),
        "business_scam": bool(re.search(r'\b(opportunity|partnership|collaboration|quick.*discussion|interested|available|venture|investment|commission|income|work.*home|exclusive.*offer|exclusive.*deal|noticed.*profile|benefit.*offer|special.*offer|selected|program)\b', raw_text, re.IGNORECASE)),
        "social_engineering": bool(re.search(r'\b(checking.*available|just.*checking|quick.*chat|available.*discuss|get.*back|can.*help|interested.*?in|looking.*?for|we.*noticed|we.*think|thought.*might|came.*across|came.*contact|share.*useful|following.*up|following.*on|reach.*out|connect.*with)\b', raw_text, re.IGNORECASE)),
        "phishing": bool(re.search(r'\b(account|review|pending|confirm.*details|verify|confirmation|avoid.*suspension|temporary.*suspension|transaction|verification|ensure.*uninterrupted|subscription|expire|renew|attached.*document)\b', raw_text, re.IGNORECASE)),
        "urgency_pressure": bool(re.search(r'\b(limited|limited.*time|quickly|today|immediately|urgent|now|expir|renew|soon|act.*now)\b', raw_text, re.IGNORECASE)),
    }
    return features

def predict(text):
    """Enhanced prediction with advanced spam detection"""
    # 0. Detect raw spam features before cleaning
    spam_features = detect_spam_features(text)
    feature_count = sum(spam_features.values())
    
    # Boost score based on feature types
    feature_score = 0
    
    # Phishing attempts = highest priority
    if spam_features.get("phishing"):
        feature_score += 0.3
    
    # Business scams + social engineering = strong combo
    if spam_features.get("business_scam") and spam_features.get("social_engineering"):
        feature_score += 0.4
    elif spam_features.get("business_scam"):
        feature_score += 0.2
        
    if spam_features.get("social_engineering"):
        feature_score += 0.25  # Increase from 0.15 to 0.25
        
    # Urgency pressure tactics
    if spam_features.get("urgency_pressure"):
        feature_score += 0.15
        
    # Money/free offers
    if spam_features.get("money_symbols"):
        feature_score += 0.2
        
    # Multiple punctuation + suspicious words
    if spam_features.get("repeated_punct") and spam_features.get("suspicious_words"):
        feature_score += 0.25
        
    feature_score += (feature_count * 0.08)  # General boost per feature
    
    # 1. Clean text
    cleaned_text = clean_text(text)

    # 2. Convert text → sequence
    seq = tokenizer.texts_to_sequences([cleaned_text])

    # ⚠️ Handle unknown / empty input
    if len(seq[0]) == 0:
        return {
            "label": "Unknown",
            "confidence": 0.0,
            "spam_features": spam_features
        }

    # 3. Padding
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding='post', truncating='post')

    # 4. Prediction
    pred = model.predict(padded, verbose=0)[0][0]
    
    # 5. Boost score based on detected spam features
    adjusted_pred = min(pred + feature_score, 1.0)
    
    # 6. Convert to label with adaptive threshold
    # Lower threshold if social engineering or business scam detected
    if spam_features.get("phishing"):
        threshold = 0.2  # Very aggressive for phishing
    elif (spam_features.get("business_scam") or spam_features.get("social_engineering")) and feature_count >= 2:
        threshold = 0.25  # Very aggressive for deceptive patterns with multiple features
    elif spam_features.get("business_scam") and spam_features.get("money_symbols"):
        threshold = 0.25
    elif spam_features.get("business_scam"):
        threshold = 0.25  # More aggressive for business scams
    elif spam_features.get("social_engineering"):
        threshold = 0.2  # More aggressive for social engineering alone
    elif feature_count >= 3:
        threshold = 0.45
    else:
        threshold = 0.5
    
    label = "Spam" if adjusted_pred > threshold else "Not Spam"

    return {
        "label": label,
        "confidence": float(round(adjusted_pred, 4)),
        "spam_features": spam_features
    }