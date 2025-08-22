from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in()

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("wrong_user", "wrong_pass")
    assert login_page.is_error_visible()
    assert "Username and password" in login_page.get_error_message()
