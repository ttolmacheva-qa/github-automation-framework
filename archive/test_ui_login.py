from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.locator("#login-button")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

def test_valid_login(page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page.get_by_text("Swag Labs")).to_be_visible()