import requests

def test_api_start_ride():
    response = requests.post("http://127.0.0.1:8000/start")
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["result"] == "RIDE_ACTIVE"
    assert data["is_locked"] == False
    
    response = requests.post("http://127.0.0.1:8000/end")
    
    finally_data = response.json()
    
    assert finally_data['result'] == "READY"
    assert finally_data["is_locked"] == True
    