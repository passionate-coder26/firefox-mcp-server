from auth.firefox_auth import get_access_token
from tools.firefox_tool import use_tool

refresh_token = input("Enter dummy refresh token: ")
client_id = input("Enter dummy client ID: ")
client_secret = input("Enter dummy client secret: ")

access_token = get_access_token(refresh_token, client_id, client_secret)

if access_token:
    print("Access token:", access_token)
    use_tool(access_token)
else:
    print("Token generation failed.")
