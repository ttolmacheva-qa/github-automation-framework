from playwright.sync_api import expect
from pages.repo_page import RepoPage
import time # Добавь импорт

def test_repo_visibility_e2e(page, api_client, username, temp_repo):
    api_response = api_client.get_repo(username, temp_repo)
    assert api_response.status_code == 200
    repo_page = RepoPage(page)
    repo_page.navigate(username, temp_repo)
    repo_page.verify_repo_is_public(temp_repo)

def test_issue_appears_in_ui(page, api_client, username, temp_repo):
    issue_title = "Critical Bug Found"
    # 1. API: Создаем задачу
    response = api_client.create_issue(username, temp_repo, title=issue_title, body="Steps to reproduce...")
    assert response.status_code == 201
    
    # 2. UI: Проверка
    repo_page = RepoPage(page)
    repo_page.navigate(username, temp_repo)
    repo_page.open_issues()

    # Ищем текст более гибко (без .first и с небольшим таймаутом)
    expect(page.get_by_text(issue_title, exact=False)).to_be_visible(timeout=10000)

def test_description_sync_e2e(page, api_client, username, temp_repo):
    description = f"Update-{int(time.time())}"

     # 1. API: Обноляем описание
    res = api_client.update_repo(username, temp_repo, description=description)
    assert res.status_code == 200

    # 2. API-ПОЛЛИНГ
    updated = False
    for _ in range(10):
        get_res = api_client.get_repo(username, temp_repo)
        if get_res.json().get("description") == description:
            updated = True
            break
        time.sleep(2)

    assert updated, "API не обновило описание!"

    # 3. UI
    repo_page = RepoPage(page)
    repo_page.navigate(username, temp_repo)
    repo_page.verify_description(description)