Feature: Product Checkout
  As a registered user
  I want to buy products from the Sauce Demo store
  So that I can complete my checkout successfully

  @smoke
  Scenario Outline: Buy a product and complete checkout
    Given the user opens the login page
    When the user logs in
    And the user adds "<product>" to the cart
    And the user proceeds to checkout
    And the user completes checkout
    Then the order should be successful

  Examples:
    | product                |
    | Sauce Labs Backpack    |
    | Sauce Labs Bike Light  |