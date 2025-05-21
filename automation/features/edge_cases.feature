Feature: Edge Case Scenarios on Digikala

  Scenario: Login with empty email and password fields
    Given I open the Digikala login page
    When I leave the email and password fields empty and click login
    Then I should see a validation error message 