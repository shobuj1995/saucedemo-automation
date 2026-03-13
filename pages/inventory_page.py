from pages.base_page import BasePage


class InventoryPage(BasePage):

    cart_icon = ".shopping_cart_link"

    def add_product(self, product_name):

        product = self.page.locator(".inventory_item").filter(has_text=product_name)
        product.get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        self.click(self.cart_icon)