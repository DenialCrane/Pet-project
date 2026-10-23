import requests

def test_check_server_status():
    response = requests.get("https://httpbin.org")        
    assert response.status_code == 200