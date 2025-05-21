# Gherkin Test Cases

## Feature: User Registration
```gherkin
Feature: User Registration
  As a new user
  I want to register on the website
  So that I can access the platform

  Scenario: Successful user registration
    Given I am on the registration page
    When I enter a valid email address
    And I enter a valid password
    And I confirm the password
    And I click the "Register" button
    Then I should be registered successfully
    And I should be redirected to the dashboard
```

## Feature: User Login
```gherkin
Feature: User Login
  As a registered user
  I want to log in to the website
  So that I can access my account

  Scenario: Successful user login
    Given I have a valid account
    When I enter my email address
    And I enter my password
    And I click the "Login" button
    Then I should be logged in successfully
    And I should be redirected to the dashboard
```

## Feature: Product Search
```gherkin
Feature: Product Search
  As a user
  I want to search for products
  So that I can find what I'm looking for

  Scenario: Search for a product
    Given I am on the homepage
    When I enter a product name in the search box
    And I click the search button
    Then I should see relevant products in the search results
``` 