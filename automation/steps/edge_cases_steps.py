from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selectors.digikala_selectors import LOGIN_PAGE

@when('I leave the email and password fields empty and click login')
def step_impl(context):
    # Ensure fields are empty
    email_input = context.driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE["email_input"])
    password_input = context.driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE["password_input"])
    email_input.clear()
    password_input.clear()
    # Click login button
    login_button = context.driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE["login_button"])
    login_button.click()

@then('I should see a validation error message')
def step_impl(context):
    try:
        # Wait for validation error (assume .error-message or similar)
        error_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE["error_message"]))
        )
        assert error_message.is_displayed()
    except:
        assert False, "Validation error message was not displayed"
    finally:
        context.driver.quit() 