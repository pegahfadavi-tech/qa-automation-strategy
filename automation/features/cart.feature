Feature: Add product to cart on Digikala

  Scenario: Add item to cart and verify cart contents
    Given I open a product page on Digikala
    When I click on add to cart
    And I go to the cart page
    Then I should see the item in the cart