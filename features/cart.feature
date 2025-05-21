Feature: Add product to cart on Digikala

  Scenario: Add item to cart and go to checkout
    Given I open a product page on Digikala
    When I click on add to cart
    Then I should see the item in the cart 