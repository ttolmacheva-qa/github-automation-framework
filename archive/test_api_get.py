import requests

def test_get_post_by_id_check_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_get_post_check_title():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data["userId"] == 1