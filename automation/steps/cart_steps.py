from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selectors.digikala_selectors import PRODUCT_PAGE, CART_PAGE, COMMON

@given('I open a product page on Digikala')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Using a real product URL from Digikala
    context.driver.get("https://www.digikala.com/product/dkp-123456/")  # Replace with actual product URL
    context.driver.maximize_window()
    
    # Wait for product page to load
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, PRODUCT_PAGE["product_title"]))
    )

@when('I click on add to cart')
def step_impl(context):
    try:
        # Wait for add to cart button to be clickable
        add_to_cart_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, PRODUCT_PAGE["add_to_cart_button"]))
        )
        add_to_cart_button.click()
        
        # Wait for loading to complete
        try:
            WebDriverWait(context.driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, COMMON["loading_spinner"]))
            )
        except:
            pass  # Loading spinner might not appear
            
        # Wait for success toast
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, COMMON["success_toast"]))
        )
    except:
        assert False, "Could not find or click the add to cart button"

@then('I should see the item in the cart')
def step_impl(context):
    try:
        # Wait for cart to be updated
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CART_PAGE["cart_items"]))
        )
        
        # Verify cart total is displayed
        cart_total = context.driver.find_element(By.CSS_SELECTOR, CART_PAGE["cart_total"])
        assert cart_total.is_displayed(), "Cart total is not displayed"
        
        # Verify checkout button is available
        checkout_button = context.driver.find_element(By.CSS_SELECTOR, CART_PAGE["checkout_button"])
        assert checkout_button.is_displayed(), "Checkout button is not displayed"
        
    except:
        assert False, "Item was not added to cart"
    finally:
        context.driver.quit() 