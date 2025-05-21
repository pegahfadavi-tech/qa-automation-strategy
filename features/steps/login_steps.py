from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from features.selectors.digikala_selectors import LOGIN_PAGE, COMMON

@given('I open the Digikala login page')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.digikala.com/users/login-register/")
    context.driver.maximize_window()
    
    # Wait for login form to be visible
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE["login_form"]))
    )
    
    # Click login tab if not already selected
    try:
        login_tab = context.driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE["login_tab"])
        if not login_tab.get_attribute("aria-selected") == "true":
            login_tab.click()
    except:
        pass  # Tab might be already selected

@when('I enter valid credentials')
def step_impl(context):
    # Wait for inputs to be visible
    email_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE["email_input"]))
    )
    password_input = context.driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE["password_input"])
    
    # Enter credentials
    email_input.send_keys("your_test_email@example.com")  # Replace with actual test credentials
    password_input.send_keys("your_test_password")  # Replace with actual test credentials
    
    # Click login button
    login_button = context.driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE["login_button"])
    login_button.click()
    
    # Wait for loading to complete
    try:
        WebDriverWait(context.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, COMMON["loading_spinner"]))
        )
    except:
        pass  # Loading spinner might not appear

@when('I enter invalid credentials')
def step_impl(context):
    # Wait for inputs to be visible
    email_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE["email_input"]))
    )
    password_input = context.driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE["password_input"])
    
    # Enter invalid credentials
    email_input.send_keys("valid_email@example.com")
    password_input.send_keys("invalid_password")
    
    # Click login button
    login_button = context.driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE["login_button"])
    login_button.click()
    
    # Wait for loading to complete
    try:
        WebDriverWait(context.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, COMMON["loading_spinner"]))
        )
    except:
        pass  # Loading spinner might not appear

@then('I should see the homepage or user profile')
def step_impl(context):
    try:
        # Wait for user account element to be visible
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE["user_account"]))
        )
        assert True
    except:
        assert False, "Login was not successful"
    finally:
        context.driver.quit()

@then('I should see an error message')
def step_impl(context):
    try:
        # Wait for error message to be visible
        error_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE["error_message"]))
        )
        assert error_message.is_displayed()
    except:
        assert False, "Error message was not displayed"
    finally:
        context.driver.quit() 