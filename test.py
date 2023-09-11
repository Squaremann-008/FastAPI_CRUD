import requests

# Define the base URL of your FastAPI application
BASE_URL = "http://127.0.0.1:8000"  

# Function to make HTTP requests and handle responses
def make_request(method, endpoint, data=None):
    url = f"{BASE_URL}{endpoint}"
    response = None
    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, json=data)
    elif method == "PUT":
        response = requests.put(url, json=data)
    elif method == "DELETE":
        response = requests.delete(url)
    return response

# Test Create (POST)
def test_create_person():
    data = {"name": "John Doe", "age": 35}
    response = make_request("POST", "/api/", data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    print("Create Person Test Passed")

# Test Read (GET) by Name
def test_read_person_by_name():
    response = make_request("GET", "/api/John Doe")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    print("Read Person Test Passed")

# Test Update (PUT)
def test_update_person():
    data = {"name": "John Doe", "age": 39}
    response = make_request("PUT", "/api/John Doe", data)
    assert response.status_code == 200
    assert response.json()["age"] == 39
    print("Update Person Test Passed")

# Test Delete (DELETE)
def test_delete_person():
    response = make_request("DELETE", "/api/John Doe")
    assert response.status_code == 200
    print("Delete Person Test Passed")

if __name__ == "__main__":
    # Run the tests
    test_create_person()
    test_read_person_by_name()
    test_update_person()
    test_delete_person()
