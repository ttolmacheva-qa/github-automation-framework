import pytest
import requests

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/posts"

def test_delete_post(base_url):
    post_id = 1
    response = requests.delete(f"{base_url}/{post_id}")
    assert response.status_code == 200

def test_get_all_posts(base_url):
    response = requests.get(base_url)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0