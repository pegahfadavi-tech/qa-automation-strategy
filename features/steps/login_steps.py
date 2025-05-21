from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@given('I open the Digikala login page')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.digikala.com/users/login-register/")
    context.driver.maximize_window()

@when('I enter valid credentials')
def step_impl(context):
    # Note: In a real implementation, you would use environment variables or a config file for credentials
    email_input = context.driver.find_element(By.NAME, "login[email_phone]")
    password_input = context.driver.find_element(By.NAME, "login[password]")
    
    email_input.send_keys("valid_email@example.com")
    password_input.send_keys("valid_password")
    
    login_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

@when('I enter invalid credentials')
def step_impl(context):
    email_input = context.driver.find_element(By.NAME, "login[email_phone]")
    password_input = context.driver.find_element(By.NAME, "login[password]")
    
    email_input.send_keys("valid_email@example.com")
    password_input.send_keys("invalid_password")
    
    login_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

@then('I should see the homepage or user profile')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".user-account"))
        )
        assert True
    except:
        assert False, "Login was not successful"
    finally:
        context.driver.quit()

@then('I should see an error message')
def step_impl(context):
    try:
        error_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message"))
        )
        assert error_message.is_displayed()
    except:
        assert False, "Error message was not displayed"
    finally:
        context.driver.quit() 