import requests

def test_get_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    response = requests.get(url)
    user_data = response.json()
    
    # Assertions for GET request
    assert response.status_code == 200
    assert user_data["name"] == "Leanne Graham"

def test_create_new_user():
    url = "https://jsonplaceholder.typicode.com/users"
    
    payload = {
        "name": "Metin QA",
        "username": "metin_tester",
        "email": "metin.automation@bursa.com"
    }
    
    response = requests.post(url, json=payload)
    new_user_data = response.json()
    
    # Assertions for POST request (Expect 201 Created)
    assert response.status_code == 201
    assert new_user_data["name"] == "Metin QA"
    assert "id" in new_user_data