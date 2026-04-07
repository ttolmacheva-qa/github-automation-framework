from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object для страницы авторизации GitHub."""

    URL = "https://github.com/login"

    # Локаторы
    USERNAME_INPUT = "#login_field"
    PASSWORD_INPUT = "#password"
    SIGN_IN_BUTTON = "input[name='commit']"
    ERROR_MESSAGE = ".js-flash-alert"

    def open(self):
        return super().open(self.URL)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.SIGN_IN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
