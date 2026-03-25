from pages.repo_page import RepoPage

def test_user_can_see_new_repo_in_ui(page, api_client, username, temp_repo):
    """
    Проверка: репозиторий, созданный через API, виден в UI GitHub.
    """
    # 1. API: Проверяем, что репозиторий создан успешно
    api_response = api_client.get_repo(username, temp_repo)
    assert api_response.status_code == 200

    # 2. UI: Переходим на страницу через Page Object
    repo_page = RepoPage(page)
    repo_page.navigate(username, temp_repo)

    # 3. UI: Проверяем видимость элементов
    repo_page.verify_repo_is_public(temp_repo)