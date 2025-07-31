# Sentiment Analysis of Text Reviews (End-to-End Application)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A full-stack, end-to-end machine learning application that analyzes the sentiment of text reviews. This project includes a trained Scikit-learn model, a Flask REST API, a Streamlit web UI, and is fully containerized with Docker for deployment.

---

### 🚀 Live Demo

**Check out the live, interactive web application here:**

**   **  <!--  This is crucial! You will build and deploy the UI later, but you can put a placeholder here for now. -->

**And here is the live API endpoint for the backend:**

**  ** <!-- e.g., https://sentiment-api-yourname.onrender.com -->

---

### 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Contact](#contact)

---

### 📖 Project Overview

This project provides a hands-on journey into Natural Language Processing (NLP) and MLOps. The goal was to build a sophisticated Sentiment Analysis application that can determine whether a piece of text (like a movie or product review) expresses a positive or negative sentiment. The project covers the entire ML lifecycle: data collection and cleaning, model training and evaluation, and finally, deployment as a containerized web service with a user-friendly interface.

---

### ✨ Features

- **Accurate Sentiment Prediction:** Utilizes a Logistic Regression model trained on the IMDb movie review dataset, achieving over 85% accuracy.
- **RESTful API:** A robust Flask API serves the model's predictions, making it accessible to any client application.
- **Interactive Web UI:** A user-friendly front-end built with Streamlit allows for easy, real-time sentiment analysis.
- **Containerized Deployment:** The entire backend service is containerized using Docker, ensuring consistency and portability across environments.
- **Cloud-Hosted:** Deployed on Render, making the application publicly and reliably accessible.

---

### 🏗️ Architecture

The application is designed with a decoupled client-server architecture:

1.  **Backend (Flask API):** A production-ready web service that handles the machine learning logic.
    - It exposes a `/predict` endpoint.
    - It loads the pre-trained TF-IDF vectorizer and Logistic Regression model.
    - It preprocesses incoming text and returns a sentiment prediction in JSON format.
    - It is containerized by Docker and run with a Gunicorn WSGI server.
2.  **Frontend (Streamlit UI):** A separate, interactive web application that acts as a client to the backend.
    - It provides a text area for user input.
    - On submission, it makes an HTTP POST request to the Flask API.
    - It receives the JSON response and displays the result in a user-friendly, color-coded format.


---

### 🛠️ Technologies Used

- **Backend:** Python, Flask, Gunicorn
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-learn, Pandas, NLTK
- **Deployment:** Docker, Render (PaaS)
- **Version Control:** Git, GitHub

---

### ⚙️ Setup and Installation

To run this project locally, please follow these steps:

**Prerequisites:**
- Python 3.9+
- Git
- Docker Desktop

**1. Clone the repository:**
```bash
git clone https://github.com/maltiadarsh/sentiment-analysis-app.git
cd sentiment-analysis-app
```
### **2. Create and activate a virtual environment:**
# For Unix/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

# For Windows
```bash
python -m venv venv
```
```bash
.\\venv\\Scripts\\activate
```
### 3.Install dependencies:
```bash
pip install -r requirements.txt
```
