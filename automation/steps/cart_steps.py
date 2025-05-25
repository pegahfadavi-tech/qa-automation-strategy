from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from automation.selectors.locators import PRODUCT_PAGE, CART_PAGE, COMMON, HEADER, BASKET_ELEMENT, BASKET_ELEMENT_NEW, \
    CART_ITEM_CHECK

@given('I open a product page on Digikala')
def open_product_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.digikala.com/product/dkp-12376940/")
    context.driver.maximize_window()

    try:
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, PRODUCT_PAGE["product_title"][1]))
        )
        print("✓ Product page loaded successfully.")
    except TimeoutException:
        raise AssertionError("Could not load product page within 20 seconds.")


@when('I click on add to cart')
def click_add_to_cart(context):
    try:
        elements = context.driver.find_elements(By.CSS_SELECTOR, PRODUCT_PAGE["add_to_cart_button"][1])
        print(f"Found {len(elements)} elements for add to cart button selector.")
        for idx, el in enumerate(elements):
            print(
                f"Element {idx}: tag={el.tag_name}, text={el.text}, enabled={el.is_enabled()}, displayed={el.is_displayed()}")
        add_to_cart_button = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, PRODUCT_PAGE["add_to_cart_button"][1]))
        )
        # Wait for overlays/spinners to disappear if present
        try:
            WebDriverWait(context.driver, 5).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, COMMON["loading_spinner"][1]))
            )
        except TimeoutException:
            pass  # Spinner might not appear
        # Scroll into view
        context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
        # Try normal click, fallback to JS click if intercepted
        try:
            add_to_cart_button.click()
        except Exception as e:
            print(f"Normal click failed: {e}, trying JS click.")
            context.driver.execute_script("arguments[0].click();", add_to_cart_button)
        print("✓ Clicked on add to cart button.")
    except TimeoutException:
        raise AssertionError("Could not find or click the add to cart button within 20 seconds.")


@when('I go to the cart page')
def go_to_cart_page(context):
    context.driver.get("https://www.digikala.com/checkout/cart/")
    print("✓ Navigated directly to the cart page.")


@then('I should see the item in the cart')
def verify_cart_items(context):
    try:
        # Debug: print all elements found for the cart item check locator
        elements = context.driver.find_elements(*CART_ITEM_CHECK)
        print(f"Found {len(elements)} elements for the cart item check XPath.")
        for idx, el in enumerate(elements):
            print(f"Element {idx}: tag={el.tag_name}, text={el.text}, displayed={el.is_displayed()}")
        # Wait for the element to appear
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located(CART_ITEM_CHECK)
        )
        print("✓ Verified: Cart item is present using the locator.")
    except TimeoutException:
        raise AssertionError("Could not verify cart items within 20 seconds.")
    finally:
        context.driver.quit()
