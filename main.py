import config


import requests
import base64

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET

def get_access_token(client_id, client_secret):
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

    token_url = "https://accounts.spotify.com/api/token"
    token_data = {"grant_type": "client_credentials"}
    token_headers = {"Authorization": f"Basic {client_creds_b64}"}

    r = requests.post(token_url, data=token_data, headers=token_headers)
    token_response_data = r.json()
    return token_response_data["access_token"]

access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
print(access_token)

def get_saved_tracks(access_token):
    url = "https://api.spotify.com/v1/me/tracks"
    headers = {"Authorization": f"Bearer {access_token}"}
    r = requests.get(url, headers=headers)
    return r.json()

saved_tracks = get_saved_tracks(access_token)
print(saved_tracks)
