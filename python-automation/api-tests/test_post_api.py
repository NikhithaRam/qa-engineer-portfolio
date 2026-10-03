import requests


def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "name": "Nikhitha",
        "email": "nikhitha@example.com"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Nikhitha"
    assert data["email"] == "nikhitha@example.com"
