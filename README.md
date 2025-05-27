# sentiment-lens

This project implements a sentiment analysis tool using a pre-trained BERT model from Hugging Face Transformers. The tool classifies input text into positive, negative, or neutral sentiments and is deployed as both a REST API and a simple Web UI.

## Project Structure

```
nlp-text-analytics-project
├── src
│   ├── main.py          # Entry point of the application (API + Web UI)
│   ├── utils.py         # Utility functions for text preprocessing
│   └── models
│       └── sentiment_model.py  # Class for loading and using the sentiment analysis model
│   └── templates
│       └── index.html   # Web UI template
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
└── tests
    └── test_sentiment.py  # Unit tests for sentiment analysis functionality
```

## Setup Instructions

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd nlp-text-analytics-project
   ```
2. **(Recommended) Create a virtual environment:**

   ```sh
   python -m venv venv
   # Activate the environment:
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

### 1. **Start the Web UI and API**

Run the following command:

```sh
python src/main.py
```

- The **Web UI** will be available at: [http://localhost:5000/](http://localhost:5000/)
- The **REST API** endpoint is at: [http://localhost:5000/predict](http://localhost:5000/predict)

### 2. **Using the Web UI**

- Open your browser and go to [http://localhost:5000/](http://localhost:5000/)
- Enter any text in the box and click "Analyze Sentiment".
- The sentiment result will be displayed below the form.

### 3. **Using the REST API**

Send a POST request to `/predict` with a JSON body:

```json
{
  "text": "I love using this product!"
}
```

You can use tools like Postman, curl, or any HTTP client.

#### Example curl command:

```sh
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"I love using this product!\"}"
```

### 4. **Running Unit Tests**

To run the unit tests:

```sh
python -m unittest discover tests
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
