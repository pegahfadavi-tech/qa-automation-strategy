# Digikala Locators
# This file contains all the locators used in the test automation

# Product Page Locators
PRODUCT_PAGE = {
    "product_title": ("xpath", '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]/div/h1'),
    "add_to_cart_button": ("css", "button[data-testid='add-to-cart']"),
    "product_price": ("xpath", '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div[1]/div[4]/div/div/div/div[1]/div[2]/div[2]/span'),
    "product_image": ("xpath", '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div/picture/img'),
    "product_description": ("xpath", '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[7]/div[2]/div[1]/article/div[2]'),
    "quantity_selector": ("css", "div[data-testid='quantity-selector']"),
    "variant_selector": ("css", "div[data-testid='variant-selector']")
}

# Cart Page Locators
CART_PAGE = {
    "cart_items": ("css", "div[data-testid='cart-items']"),
    "cart_total": ("css", "div[data-testid='cart-total']"),
    "checkout_button": ("css", "button[data-testid='checkout-button']"),
    "cart_item_title": ("css", "div[data-testid='cart-item-title']"),
    "cart_item_price": ("css", "div[data-testid='cart-item-price']"),
    "cart_item_quantity": ("css", "div[data-testid='cart-item-quantity']"),
    "remove_item_button": ("css", "button[data-testid='remove-item-button']"),
    "empty_cart_message": ("css", "div[data-testid='empty-cart-message']"),
    "go_to_cart_button": ("xpath", "//button[contains(text(), 'برو به سبد خرید')]")
}

# Common Locators
COMMON = {
    "loading_spinner": ("css", "div[data-testid='loading-spinner']"),
    "success_toast": ("css", "div[data-testid='success-toast']"),
    "error_toast": ("css", "div[data-testid='error-toast']"),
    "modal_close_button": ("css", "button[data-testid='modal-close-button']"),
    "notification_badge": ("css", "span[data-testid='notification-badge']")
}

# Login Page Locators
LOGIN_PAGE = {
    "login_form": ("css", "form[data-testid='login-form']"),
    "login_tab": ("css", "button[data-testid='login-tab']"),
    "email_input": ("css", "input[data-testid='email-input']"),
    "password_input": ("css", "input[data-testid='password-input']"),
    "login_button": ("css", "button[data-testid='login-button']"),
    "error_message": ("css", "div[data-testid='error-message']")
}

# Header Locators
HEADER = {
    "search_input": ("css", "input[data-testid='search-input']"),
    "search_button": ("css", "button[data-testid='search-button']"),
    "cart_icon": ("css", "button[data-testid='cart-icon']"),
    "user_menu": ("css", "button[data-testid='user-menu']"),
    "login_link": ("css", "a[data-testid='login-link']")
}

# New Locator
BASKET_ELEMENT = ("xpath", "//a[@href='/checkout/cart']")

# Added basket_element locator
BASKET_ELEMENT_NEW = ("xpath", "/html/body/div[1]/div[1]/div[1]/header/div[2]/div/div/div[2]/div[2]/a/div[1]/svg")

# Added cart item check locator
CART_ITEM_CHECK = ("xpath", "/html/body/div/div[1]/div[3]/div[3]/div[2]/ul[2]/li/div[1]/div/section/div[2]/div/div[1]/div/div/div/div/div/div/p/span/div/div/span") 