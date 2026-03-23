import pytest
import os
import time
from dotenv import load_dotenv
from api.github_client import GitHubClient
from playwright.sync_api import expect # Не забываем про проверки UI

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")
client = GitHubClient(TOKEN)

@pytest.fixture
def public_repo():
    # SETUP: Создаем ПУБЛИЧНЫЙ репозиторий
    repo_name = f"e2e-test-repo-{int(time.time())}"
    client.create_repo(repo_name, private=False) # private=False для UI теста
    print(f"\n[API] Создан публичный репозиторий: {repo_name}")

    yield repo_name

    # TEARDOWN: Удаляем
    client.delete_repo(USERNAME, repo_name)
    print(f"\n[API] Репозиторий {repo_name} удален")

def test_repo_is_visible_in_ui(page, public_repo):
    # page - фикстура Playwright
    # public_repo - наша фикстура, создающая данные через API

    # 1. Формируем URL страницы репозитория
    repo_url = f"https://github.com/{USERNAME}/{public_repo}"

    # 2. Переходим на страницу через Playwright
    page.goto(repo_url)
    print(f"[UI] Переход на страницу: {repo_url}")

    # 3. Проверяем, что на странице есть заголовок с именем репо
    # На GitHub bvz репо обычно находится в ссылке с атрибутами data-pjax="#repo-content-зофч-container"
    # Но мы можем просто найти текст имени репозитория
    expect(page.get_by_text(public_repo)).to_be_visible()

    # 4. Проверим, что на странице есть плашка "Public"
    expect(page.get_by_text("Public", exact=True).first).to_be_visible()