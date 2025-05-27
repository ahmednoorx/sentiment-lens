from flask import Flask, request, jsonify, render_template
from models.sentiment_model import SentimentModel
from utils import preprocess_text

app = Flask(__name__, template_folder="templates")
model = SentimentModel()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    processed_text = preprocess_text(text)
    sentiment = model.predict(processed_text)
    return jsonify({'sentiment': sentiment})

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_text = request.form.get('user_text', '')
        processed_text = preprocess_text(user_text)
        result = model.predict(processed_text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)