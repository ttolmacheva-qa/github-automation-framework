from pages.base_page import BasePage


class ProfilePage(BasePage):
    """Page Object для страницы профиля пользователя."""

    # Локаторы
    REPO_LIST = "[data-filterable-for='your-repos-filter']"
    REPO_LINK = "a[itemprop='name codeRepository']"
    BIO_ELEMENT = "[data-bio-text]"

    def open(self, username: str = ""):
        url = f"https://github.com/{username}" if username else "https://github.com"
        return super().open(url)

    def has_repo(self, repo_name: str) -> bool:
        """Проверяет, отображается ли репозиторий в профиле."""
        repos = self.page.locator(self.REPO_LINK).all_text_contents()
        return repo_name in [r.strip() for r in repos]

    def get_repo_names(self) -> list[str]:
        """Возвращает список имён репозиториев."""
        return [r.strip() for r in self.page.locator(self.REPO_LINK).all_text_contents()]
