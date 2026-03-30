import pytest
from pytest_bdd import scenario, given, when, then, parsers

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# # Use the Scenario Outline name, not specific products
# @scenario("../features/checkout.feature", "Buy a product and complete checkout")
# @pytest.mark.smoke
# def test_checkout():
#     """This will run once for each product in the Examples table"""
#     pass

import pytest
from pytest_bdd import scenario, given, when, then, parsers

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@scenario("../features/checkout.feature", "Buy a product and complete checkout")
@pytest.mark.smoke
def test_checkout():
    """This will run once for each product in the Examples table"""
    pass


@given("the user opens the login page")
def open_login(page):
    login = LoginPage(page)
    login.open_login_page()


@when("the user logs in")
def login_user(page):
    login = LoginPage(page)
    login.login()


@when(parsers.parse('the user adds "{product}" to the cart'))
def add_product(page, product):
    """Dynamically adds the product from Examples table"""
    inventory = InventoryPage(page)
    inventory.add_product(product)
    inventory.open_cart()


@when("the user proceeds to checkout")
def proceed_checkout(page):
    cart = CartPage(page)
    cart.click_checkout()


@when("the user completes checkout")
def complete_checkout(page):
    checkout = CheckoutPage(page)
    checkout.enter_checkout_info()
    checkout.finish_order()


@then("the order should be successful")
def verify_success(page):
    checkout = CheckoutPage(page)
    success_message = checkout.get_success_message()
    assert "Thank you" in success_message, f"Expected 'Thank you' in '{success_message}'"


@given("the user opens the login page")
def open_login(page):
    login = LoginPage(page)
    login.open_login_page()


@when("the user logs in")
def login_user(page):
    login = LoginPage(page)
    login.login()


@when(parsers.parse('the user adds "{product}" to the cart'))
def add_product(page, product):
    """Dynamically adds the product from Examples table"""
    inventory = InventoryPage(page)
    inventory.add_product(product)
    inventory.open_cart()


@when("the user proceeds to checkout")
def proceed_checkout(page):
    cart = CartPage(page)
    cart.click_checkout()


@when("the user completes checkout")
def complete_checkout(page):
    checkout = CheckoutPage(page)
    checkout.enter_checkout_info()
    checkout.finish_order()


@then("the order should be successful")
def verify_success(page):
    checkout = CheckoutPage(page)
    success_message = checkout.get_success_message()
    assert "Thank you" in success_message, f"Expected 'Thank you' in '{success_message}'"