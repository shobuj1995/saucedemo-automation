from pages.base_page import BasePage


class CheckoutPage(BasePage):

    first_name = "#first-name"
    last_name = "#last-name"
    zip_code = "#postal-code"
    continue_btn = "#continue"
    finish_btn = "#finish"
    success_msg = ".complete-header"

    def enter_checkout_info(self):

        self.type(self.first_name, "John")
        self.type(self.last_name, "Doe")
        self.type(self.zip_code, "10001")

        self.click(self.continue_btn)

    def finish_order(self):
        self.click(self.finish_btn)

    def get_success_message(self):
        return self.get_text(self.success_msg)