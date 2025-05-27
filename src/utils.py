def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and special characters
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    
    return text

def tokenize_text(text):
    # Simple tokenization by splitting on whitespace
    return text.split()

def normalize_text(text):
    # Preprocess the text by normalizing and tokenizing
    preprocessed_text = preprocess_text(text)
    tokens = tokenize_text(preprocessed_text)
    return tokens