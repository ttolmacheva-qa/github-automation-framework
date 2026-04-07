from pages.base_page import BasePage


class RepoPage(BasePage):
    """Page Object для страницы репозитория."""
    def __init__(self, page: Page):
        self.page = page
        self.issues_tab = page.get_by_role("link", name="Issues")
        self.public_label = page.get_by_text("Public", exact=True).first

    def navigate(self, owner, repo_name):
        self.page.goto(f"https://github.com/{owner}/{repo_name}")
        self.page.wait_for_load_state("networkidle")

    def verify_repo_is_public(self, repo_name):
        expect(self.page.get_by_text(repo_name).first).to_be_visible()
        expect(self.public_label).to_be_visible()
    
    def open_issues(self):
        self.issues_tab.click()
        self.page.wait_for_load_state("networkidle")

    def verify_description(self, text):
        description_locator = self.page.get_by_text(text, exact=False)
        try:
            expect(description_locator).to_be_visible(timeout=10000)
        except AssertionError:
            print(f"\n[UI] Текст '{text}' не найдено. Делаю скриншот и перезагружаю...")
            self.page.screenshot(path="debug_screenshot.png")
            self.page.reload()
            self.page.wait_for_load_state("networkidle")
            expect(description_locator).to_be_visible(timeout=15000)
