import pytest
import os
import time
from dotenv import load_dotenv
from api.github_client import GitHubClient

load_dotenv()

@pytest.fixture(scope="session")
def api_client():
    token = os.getenv("GITHUB_TOKEN")
    return GitHubClient(token)

@pytest.fixture(scope="session")
def username():
    return os.getenv("GITHUB_USERNAME")

@pytest.fixture
def temp_repo(api_client, username):
    repo_name = f"auto-repo-{int(time.time())}"
    api_client.create_repo(repo_name, private=False)

    api_client.create_file(username, repo_name, "README.md", "# My Test Repo", "initial commit")

    print(f"\n[API] Создан репозиторий с файлом: {repo_name}")
    yield repo_name # Отдаем имя тесту
    api_client.delete_repo(username, repo_name)