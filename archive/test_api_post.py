import requests

def test_create_post():
    payload = {
        "title": "Мой крутой пост",
        "body": "Тут много текста",
        "userId": 1
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == "Мой крутой пост"
    assert response_data["id"] == 101