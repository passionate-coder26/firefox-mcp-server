import requests

DUMMY_TOKEN_URL = "http://localhost:8000/oauth/token"  # Replace later with real one

def get_access_token(refresh_token, client_id, client_secret):
    """
    Simulates getting an access token using a refresh token.
    Replace DUMMY_TOKEN_URL with the real endpoint later.
    """
    print("[AUTH] Requesting new access token...")

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    try:
        response = requests.post(DUMMY_TOKEN_URL, data=payload)
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get("access_token")
            print("[AUTH] Access token retrieved successfully.")
            return access_token
        else:
            print(f"[AUTH] Failed to get token. Status: {response.status_code}, Body: {response.text}")
            return None
    except Exception as e:
        print(f"[AUTH] Exception occurred: {e}")
        return None
