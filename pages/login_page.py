class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.username_input = self.page.locator("input[data-test='username']")
        self.password_input = self.page.locator("input[data-test='password']")
        self.login_button = self.page.locator("input[data-test='login-button']")
        self.error_message = self.page.locator("h3[data-test='error']")

    # Actions methods
    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        """Composite action to login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Validations / Getters
    def is_error_visible(self) -> bool:
        return self.error_message.is_visible()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    def is_logged_in(self) -> bool:
        """Check if login was successful by URL."""
        return self.page.url.endswith("/inventory.html")
