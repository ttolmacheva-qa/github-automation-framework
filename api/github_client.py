import requests
import base64

class GitHubClient:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def _get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
    
    def _post(self, endpoint,payload):
        return requests.post(f"{self.base_url}{endpoint}", json=payload, headers=self.headers)
    
    def _delete(self,endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)

    def create_repo(self, name, private=True):
        return self._post("/user/repos", {"name": name, "private":private})
    
    def delete_repo(self, owner, repo_name):
        """Метод удаления репозитория"""
        # Было {name}, должно быть {repo_name}
        return self._delete(f"/repos/{owner}/{repo_name}")
    
    def get_repo(self, owner, repo_name):
        """Метод для получения данных о репозитории"""
        # Было {name}, должно быть {repo_name}
        return self._get(f"/repos/{owner}/{repo_name}")
    
    def update_repo(self, owner, repo_name, description):
        return requests.patch(
            f"{self.base_url}/repos/{owner}/{repo_name}",
            json={"description": description},
            headers=self.headers
        )
    
    def create_issue(self, owner, repo_name, title, body):
        """Создание Issue в репозитории"""
        return requests.post(
            f"{self.base_url}/repos/{owner}/{repo_name}/issues",
            json={"title": title, "body": body},
            headers=self.headers
        )
    
    def get_issues(self, owner, repo_name):
        """Получение списка всех Issue"""
        return requests.get(
            f"{self.base_url}/repos/{owner}/{repo_name}/issues",
            headers=self.headers
        )
    
    def create_file(self, owner, repo_name, path, content, message):
        encoded_content = base64.b64encode(content.encode()).decode()

        payload = {
            "message": message,
            "content": encoded_content
        }
        return requests.put(
            f"{self.base_url}/repos/{owner}/{repo_name}/contents/{path}",
            json=payload,
            headers=self.headers
        )