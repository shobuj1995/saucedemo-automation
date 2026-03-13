from pages.base_page import BasePage


class CartPage(BasePage):

    checkout_btn = "#checkout"

    def click_checkout(self):
        self.click(self.checkout_btn)