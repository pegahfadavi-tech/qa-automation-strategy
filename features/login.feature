Feature: User Login on Digikala

  Scenario: Successful login
    Given I open the Digikala login page
    When I enter valid credentials
    Then I should see the homepage or user profile

  Scenario: Failed login with incorrect password
    Given I open the Digikala login page
    When I enter invalid credentials
    Then I should see an error message 