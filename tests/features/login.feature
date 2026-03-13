Feature: Login functionality

Scenario: Successful login
    Given user opens the login page
    When user logs in with valid credentials
    Then user should see the inventory page