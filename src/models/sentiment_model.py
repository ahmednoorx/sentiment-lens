class SentimentModel:
    def __init__(self, model_name='nlptown/bert-base-multilingual-uncased-sentiment'):
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def predict(self, text):
        import torch

        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        logits = outputs.logits
        predicted_class = logits.argmax(dim=1).item()
        # Map model output to human-friendly labels (1-5 stars)
        label_map = {
            0: "Very Negative",
            1: "Negative",
            2: "Neutral",
            3: "Positive",
            4: "Very Positive"
        }
        return label_map.get(predicted_class, str(predicted_class))