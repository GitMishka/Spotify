import webbrowser
import requests
import base64
import config

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET

def get_user_authorization(client_id, redirect_uri, scope):
    auth_url = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
    webbrowser.open(auth_url)

def get_access_token_with_code(client_id, client_secret, code, redirect_uri):
    token_url = "https://accounts.spotify.com/api/token"
    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }
    client_creds_b64 = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    token_headers = {"Authorization": f"Basic {client_creds_b64}"}

    r = requests.post(token_url, data=token_data, headers=token_headers)
    token_response_data = r.json()

    if 'access_token' in token_response_data:
        return token_response_data["access_token"]
    else:
        print("Error in token response:", token_response_data)
        return None

scope = "user-library-read"  # Modify scopes as needed
redirect_uri = "http://localhost/"  # Must match the one set in Spotify Developer Dashboard
get_user_authorization(CLIENT_ID, redirect_uri, scope)
#BQDTC0hxn7wMt35EpSrSBxfoVtr07KHKQQ5-MgGOsDkWMJvypJXzTyCqX5hS94pvLxd6wHd0uCUyjEBFutG0gDw1tjIZuxfYOQ4NerkxTkYe6FM3ea38eORlw_6grugZ1Uheqo9_d4G041Q3ZueEhoDdll2nbrQNfMzJHwWAFTRFrGlHhCo1LFQ1PVw
# After getting the code from the redirect URL manually, replace 'code_from_query_string' with the actual code
code = "AQD_cGynVVELOx6n8emXZTW7LRiqWYOD5bF6BMjTyb5zQ7wEjg0kb9XyrTuh0Lbs3WiA2JUYw6TFUgGO8i3XnPcltwo49ZbC9kn6XgVzocYar1W82bzMFsOWnH5T9llZub7apeQJywbnl9j3RdkOMP-aChZdUXfIiVczzzYH5vGeR7pSCKMHKA"
access_token = get_access_token_with_code(CLIENT_ID, CLIENT_SECRET, code, redirect_uri)

if access_token:
    print("Access Token:", access_token)
else:
    print("Failed to get access token")
