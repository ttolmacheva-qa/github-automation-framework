import requests

class GitHubClient:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        # Заголовки храняться в одном месте!
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def create_repo(self, name, private=True): # Добавили значение по умолчанию
        payload = {
            "name": name,
            "private": private # Теперь берем из аргумента
        }
        response = requests.post(f"{self.base_url}/user/repos", json=payload, headers=self.headers)
        return response
    
    def delete_repo(self, owner, repo_name):
        """Метод для удаления репозитория"""
        response = requests.delete(
            f"{self.base_url}/repos/{owner}/{repo_name}",
            headers=self.headers
        )
        return response
    
    def get_repo(self, owner, repo_name):
        """Метод для получения данных о репозитории"""
        response = requests.get(
            f"{self.base_url}/repos/{owner}/{repo_name}",
            headers=self.headers # ТУТ ТВОЙ ТОКЕН!
        )
        return response