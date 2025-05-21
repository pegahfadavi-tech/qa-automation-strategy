"""
Digikala selectors for UI automation
These selectors are based on the actual Digikala website structure
"""

# Login page selectors
LOGIN_PAGE = {
    "email_input": "input[name='login[email_phone]']",
    "password_input": "input[name='login[password]']",
    "login_button": "button[type='submit']",
    "error_message": ".error-message",
    "user_account": ".user-account",
    "login_form": "#login-form",
    "login_tab": "button[data-testid='login-tab']",
    "register_tab": "button[data-testid='register-tab']"
}

# Product page selectors
PRODUCT_PAGE = {
    "add_to_cart_button": "button[data-testid='add-to-cart-button']",
    "product_title": "h1[data-testid='product-title']",
    "product_price": "div[data-testid='product-price']",
    "quantity_selector": "div[data-testid='quantity-selector']",
    "color_selector": "div[data-testid='color-selector']",
    "size_selector": "div[data-testid='size-selector']",
    "seller_name": "div[data-testid='seller-name']",
    "product_gallery": "div[data-testid='product-gallery']"
}

# Cart page selectors
CART_PAGE = {
    "cart_items": "div[data-testid='cart-item']",
    "cart_total": "div[data-testid='cart-total']",
    "checkout_button": "button[data-testid='checkout-button']",
    "quantity_input": "input[data-testid='quantity-input']",
    "remove_item_button": "button[data-testid='remove-item']",
    "cart_empty_message": "div[data-testid='cart-empty-message']",
    "continue_shopping_button": "button[data-testid='continue-shopping']"
}

# Header selectors
HEADER = {
    "search_input": "input[data-testid='search-input']",
    "search_button": "button[data-testid='search-button']",
    "cart_icon": "div[data-testid='cart-icon']",
    "user_menu": "div[data-testid='user-menu']",
    "login_button": "button[data-testid='login-button']"
}

# Common selectors
COMMON = {
    "loading_spinner": "div[data-testid='loading-spinner']",
    "error_toast": "div[data-testid='error-toast']",
    "success_toast": "div[data-testid='success-toast']",
    "modal_close": "button[data-testid='modal-close']"
} 