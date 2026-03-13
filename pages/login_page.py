from pages.base_page import BasePage
from utils.config_reader import Config


class LoginPage(BasePage):

    username = "#user-name"
    password = "#password"
    login_button = "#login-button"

    def open_login_page(self):
        self.navigate(Config.BASE_URL)

    def login(self):
        self.type(self.username, Config.USERNAME)
        self.type(self.password, Config.PASSWORD)
        self.click(self.login_button)