from playwright.sync_api import Page, expect

class RepoPage:
    def __init__(self, page: Page):
        self.page = page
        # Локаторы
        self.repo_title = page.locator("#firstHeading")
        self.public_label = page.get_by_text("Public", exact=True).first


    def navigate(self, owner, repo_name):
        self.page.goto(f"https://github.com/{owner}/{repo_name}")

    def verify_repo_is_public(self, repo_name):
        expect(self.page.get_by_text(repo_name)).to_be_visible()
        expect(self.public_label).to_be_visible()