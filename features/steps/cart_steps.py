from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@given('I open a product page on Digikala')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Note: In a real implementation, you would use a specific product URL
    context.driver.get("https://www.digikala.com/product/dkp-123456/")
    context.driver.maximize_window()

@when('I click on add to cart')
def step_impl(context):
    try:
        add_to_cart_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-to-cart-button']"))
        )
        add_to_cart_button.click()
    except:
        assert False, "Could not find or click the add to cart button"

@then('I should see the item in the cart')
def step_impl(context):
    try:
        # Wait for the cart to be updated
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-item"))
        )
        assert True
    except:
        assert False, "Item was not added to cart"
    finally:
        context.driver.quit() 