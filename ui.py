# --- This code should already be in your ui.py file ---
import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/predict"

st.title("Sentiment Analysis of Text Reviews")

user_input = st.text_area(
    label="Enter the review text below:",
    placeholder="This movie was fantastic and the acting was superb! I would highly recommend it to everyone.",
    height=150
)

analyze_button = st.button("Analyze Sentiment")

if analyze_button:
    if user_input.strip():
        payload = {'review': user_input}

        try:
            with st.spinner('Analyzing...'):
                response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                response_data = response.json()
                sentiment = response_data.get('sentiment')

                # --- UPDATE THE LOGIC INSIDE THIS BLOCK ---
                
                # 5. Display the result with visual flair.
                # We check the sentiment string and display a different, color-coded
                # message and emoji for each case.
                if sentiment == 'Positive':
                    # st.success() displays the message in a green box.
                    # We use an f-string to easily combine our text and the emoji.
                    st.success(f"Prediction: Positive 👍")
                elif sentiment == 'Negative':
                    # st.error() displays the message in a red box.
                    st.error(f"Prediction: Negative 👎")
                else:
                    # A neutral message for any unexpected response.
                    st.warning("Could not determine the sentiment. Please try another review.")
                    
            else:
                try:
                    error_details = response.json()
                    st.error(f"API Error: {error_details.get('error', 'An unknown error occurred.')}")
                except requests.exceptions.JSONDecodeError:
                    st.error(f"API Error: Status code {response.status_code} - {response.text}")

        except requests.exceptions.ConnectionError:
            st.error(f"Connection Error: Could not connect to the API at {API_URL}. Please ensure the Flask server (app.py) is running.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

    else:
        st.warning("Please enter a review to analyze.")