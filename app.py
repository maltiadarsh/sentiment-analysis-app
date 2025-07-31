from flask import Flask, request, jsonify  # type: ignore
import joblib  # type: ignore
import numpy as np
import re
import os
import nltk
from nltk.corpus import stopwords  # type: ignore
from nltk.stem import WordNetLemmatizer  # type: ignore

# Download required NLTK resources if not already present
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

try:
    lemmatizer = WordNetLemmatizer()
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# Load the trained model and TF-IDF vectorizer
try:
    model = joblib.load(os.path.join('notebooks', 'lr_model.pkl'))
    vectorizer = joblib.load(os.path.join('notebooks', 'tfidf_vectorizer.pkl'))
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError:
    print("Error: Model or vectorizer file not found.")
    model = None
    vectorizer = None
except Exception as e:
    print(f"Error loading model/vectorizer: {e}")
    model = None
    vectorizer = None

def preprocess_text(text):
    """
    Cleans and preprocesses the input text for vectorization.
    """
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(cleaned_tokens)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Sentiment Analysis API is running.'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return jsonify({'error': 'Model or vectorizer not loaded.'}), 500

    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'No JSON data received.'}), 400
    except Exception as e:
        return jsonify({'error': f'Error parsing JSON: {str(e)}'}), 400

    review_text = data.get('review')
    if not review_text or not isinstance(review_text, str) or not review_text.strip():
        return jsonify({'error': 'The "review" field is missing, empty, or not a string.'}), 400

    cleaned_text = preprocess_text(review_text)

    try:
        text_vector = vectorizer.transform([cleaned_text])
    except Exception as e:
        return jsonify({'error': f'Text vectorization failed: {str(e)}'}), 500

    try:
        prediction = model.predict(text_vector)
        sentiment = prediction[0]
        # Optional: Confidence if model supports predict_proba
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(text_vector)[0]
            confidence = round(max(proba), 3)
            return jsonify({'sentiment': sentiment.title(), 'confidence': confidence}), 200
        return jsonify({'sentiment': sentiment.title()}), 200
    except Exception as e:
        return jsonify({'error': f'Model prediction failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
