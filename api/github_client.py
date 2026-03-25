import requests

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