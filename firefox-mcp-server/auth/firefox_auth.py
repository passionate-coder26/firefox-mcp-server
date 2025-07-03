import requests

def get_access_token(refresh_token, client_id, client_secret):
    url = "https://firefox-mcp.example.com/oauth/token"  # Replace with real URL
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json().get("access_token")
