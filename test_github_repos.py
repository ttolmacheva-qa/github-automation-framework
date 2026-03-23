import requests
import pytest
import os
import time # Добавим для уникальности имен
from dotenv import load_dotenv
from api.github_client import GitHubClient

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")
client = GitHubClient(TOKEN)

# Эта фикстура будет готовить нам "песочницу" для каждого теста
@pytest.fixture
def temp_repo():
    # 1. SETUP: Создаем уникальное имя
    repo_name = f"temp-repo-{int(time.time())}"
    client.create_repo(repo_name)
    print(f"\n[Setup] Репозиторий {repo_name} создан")

    # 2. ОТДАЕМ данные тесту
    yield repo_name

    # 3. TEARDOWN: Этот код выполниться ПОСЛЕ теста, что бы ни случилось
    client.delete_repo(USERNAME, repo_name)
    print(f"\n[Teardown] Репозиторий {repo_name} удален")

# А теперь сам тест. Он стал коротким и проверяет только суть!
def test_new_repo_is_searchable(temp_repo):
    # Теперь мы используем клиента, который "знает" наш токен
    response = client.get_repo(USERNAME, temp_repo)

    assert response.status_code == 200
    assert response.json()["name"] == temp_repo