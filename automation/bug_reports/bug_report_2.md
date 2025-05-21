# Bug Report: Cart Total Not Updated After Quantity Change

## Bug Description
When changing the quantity of items in the shopping cart, the total price is not automatically updated to reflect the new quantity.

## Severity
Medium - Affects shopping experience but doesn't block purchase

## Steps to Reproduce
1. Add a product to the cart
2. Navigate to the cart page
3. Change the quantity of the item using the quantity selector
4. Observe the total price

## Expected Result
- The total price should update immediately to reflect the new quantity
- The subtotal and final price should be recalculated

## Actual Result
- The total price remains unchanged
- User needs to refresh the page to see the updated total
- The API call to update quantity is successful, but the UI is not updated

## Environment
- Browser: Chrome 120.0.6099.130
- OS: macOS Sonoma 14.2
- Device: Desktop

## Screenshots
[Attach relevant screenshots here]

## Additional Notes
- This issue occurs with all product types
- The cart API endpoints are working correctly
- The issue appears to be related to frontend state management 