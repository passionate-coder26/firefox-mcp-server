import requests

def run_firefox_mcp_tool(access_token):
    url = "https://firefox-mcp.example.com/api/tool"  # Replace with real API
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
