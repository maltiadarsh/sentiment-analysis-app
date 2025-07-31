# Import the requests library, which is the standard for making HTTP requests in Python.
import requests 

# Define the URL of your local Flask API endpoint.
# Make sure your Flask server (app.py) is running before you run this script.
API_URL = 'http://127.0.0.1:5000/predict'

# Let's create two test cases: one clearly positive and one clearly negative.
positive_review = {
    "review": "This movie was absolutely brilliant! The acting was superb and the plot was engaging from start to finish."
}

negative_review = {
    "review": "What a complete waste of time. The plot was predictable and the characters were incredibly boring."
}

def test_sentiment(review_data, expected_sentiment):
    """
    A helper function to send a request to the API and check the response.
    """
    print(f"--- Testing review: '{review_data['review'][:30]}...' ---")
    try:
        # Use requests.post() to send a POST request.
        # - The first argument is the URL.
        # - The 'json' parameter takes a Python dictionary and automatically handles
        #   converting it to a JSON string and setting the 'Content-Type' header.
        response = requests.post(API_URL, json=review_data)

        # We can check the HTTP status code of the response. 200 means 'OK'.
        print(f"Status Code: {response.status_code}")

        # If the request was successful, parse the JSON response and print it.
        if response.status_code == 200:
            response_data = response.json()
            print(f"Received Data: {response_data}")
            # Check if the prediction matches what we expect.
            if response_data.get('sentiment') == expected_sentiment:
                print("Prediction matches expected result. Test PASSED! ✅")
            else:
                print("Prediction does NOT match expected result. Test FAILED! ❌")
        else:
            # If the status code is not 200, something went wrong. Print the error content.
            print(f"Error: {response.text}")

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: Could not connect to the server at {API_URL}.")
        print("Please make sure your Flask app (app.py) is running in another terminal.")
    
    print("-" * 40 + "\\n")

# --- Run the tests ---
if __name__ == '__main__':
    test_sentiment(positive_review, "Positive")
    test_sentiment(negative_review, "Negative")
