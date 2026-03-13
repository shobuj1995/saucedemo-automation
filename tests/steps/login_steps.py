from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage


@scenario("../features/login.feature", "Successful login")
def test_login():
    pass


@given("user opens the login page")
def open_login(page):
    login = LoginPage(page)
    login.open()


@when("user logs in with valid credentials")
def do_login(page):
    login = LoginPage(page)
    login.login("standard_user", "secret_sauce")


@then("user should see the inventory page")
def verify(page):
    assert "inventory" in page.url