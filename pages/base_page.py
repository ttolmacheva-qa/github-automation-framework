from playwright.sync_api import Page


class BasePage:
    """Базовый класс для всех Page Objects."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)
        return self

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_selector(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector) or ""

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
