# Import the 'requests' library to send HTTP requests to Firebase's REST API
import requests

# Your Firebase Web API Key (unique to your Firebase project)
# This key allows your app to communicate with Firebase Authentication


API_KEY = "YOUR_API_KEY" #Your API Key


# -------------------------------
# Function: signup
# -------------------------------
def signup(email, password):
    """
    Registers a new user in Firebase Authentication using email and password.
    Returns the response from Firebase as a dictionary.
    """

    # Firebase REST API endpoint for signing up users
    # The API key is included in the URL for authentication
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"

    # The data to send in the POST request (Firebase expects JSON)
    payload = {
        "email": email,                # User's email
        "password": password,          # User's password
        "returnSecureToken": True      # Tells Firebase to return an ID token if successful
    }

    # Send the POST request to Firebase with the payload as JSON
    response = requests.post(url, json=payload)

    # Convert the response to JSON format (a Python dictionary) and return it
    return response.json()


# -------------------------------
# Function: login
# -------------------------------
def login(email, password):
    """
    Logs in an existing user using Firebase Authentication.
    Returns the response from Firebase as a dictionary.
    """

    # Firebase REST API endpoint for signing in users with email and password
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

    # The data to send in the POST request
    payload = {
        "email": email,                # User's email
        "password": password,          # User's password
        "returnSecureToken": True      # Firebase will return a secure token for authentication
    }

    # Send the POST request to Firebase
    response = requests.post(url, json=payload)

    # Return the JSON response (which contains either success data or error info)
    return response.json()
