from tools.firefox_tool import use_tool

def test_use_tool():
    token = "dummy-access-token-12345"
    try:
        use_tool(token)
        assert True
    except Exception as e:
        assert False, f"Tool crashed: {e}"
