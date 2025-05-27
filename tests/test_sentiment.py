import unittest
from src.models.sentiment_model import SentimentModel

class TestSentimentModel(unittest.TestCase):
    def setUp(self):
        self.model = SentimentModel()

    def test_positive_sentiment(self):
        text = "I love this product! It's amazing."
        prediction = self.model.predict(text)
        self.assertEqual(prediction, "positive")

    def test_negative_sentiment(self):
        text = "I hate this product. It's the worst."
        prediction = self.model.predict(text)
        self.assertEqual(prediction, "negative")

    def test_neutral_sentiment(self):
        text = "This product is okay, not great but not bad."
        prediction = self.model.predict(text)
        self.assertEqual(prediction, "neutral")

if __name__ == '__main__':
    unittest.main()