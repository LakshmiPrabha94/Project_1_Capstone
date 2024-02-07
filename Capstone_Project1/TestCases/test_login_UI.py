"""

Test Objective: Validate the user interface elements of the login page on the OrangeHRM portal.
Expected Results: The user interface elements of the login page on the OrangeHRM portal should be designed as per requirements.

"""
# Import necessary modules and classes
import pytest
from Data import data
from Locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  Automation_Scripts.login import Login


@pytest.fixture
def login_instance():
    login = Login()
    login.booting_function()
    yield login  # Provide the instance to the test


def test_username_visibility(login_instance):
    username = WebDriverWait(login_instance.driver, 30).until(EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
    assert username.is_displayed() == 'False'

def test_username_isenabled(login_instance):
    username = WebDriverWait(login_instance.driver, 30).until(EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
    assert username.is_enabled()

def test_username_isselected(login_instance):
    username = WebDriverWait(login_instance.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
    assert not username.is_selected()

def test_cursor_on_username(login_instance):
    username = WebDriverWait(login_instance.driver, 10).until(EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
    active_element = login_instance.driver.switch_to.active_element
    assert not username == active_element

def test_password_visibility(login_instance):
    password = WebDriverWait(login_instance.driver, 30).until(EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
    assert not password.is_displayed()

def test_password_isenabled(login_instance):
    password = WebDriverWait(login_instance.driver, 30).until(EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
    assert password.is_enabled()

def test_password_isselected(login_instance):
    password = WebDriverWait(login_instance.driver, 10).until(EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
    assert not password.is_selected()

def test_cursor_on_password(login_instance):
    password = WebDriverWait(login_instance.driver, 10).until(EC.visibility_of_element_located((By.NAME, locators.WebLocators().password_locator)))
    active_element = login_instance.driver.switch_to.active_element
    assert not password == active_element

def test_login_button_visibility(login_instance):
    login_button = WebDriverWait(login_instance.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
    assert not login_button.is_displayed()

def test_login_button_isenabled(login_instance):
    login_button = WebDriverWait(login_instance.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
    assert login_button.is_enabled()

def test_login_button_isselected(login_instance):
    login_button = WebDriverWait(login_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
    assert not login_button.is_selected()

def test_cursor_on_login_button(login_instance):
    login_button = WebDriverWait(login_instance.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().login_button_locator)))
    active_element = login_instance.driver.switch_to.active_element
    assert not login_button == active_element

def test_verify_password_masked(login_instance):

    # Enter username and password
    username_field = WebDriverWait(login_instance.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator)))
    username_field.send_keys(data.WebData().username)
    password_field = WebDriverWait(login_instance.driver, 3).until(
        EC.element_to_be_clickable((By.NAME, locators.WebLocators().password_locator))
    )
    password_field.send_keys(data.WebData().password)

    # Check password field's "type" attribute directly
    password_type = password_field.get_attribute("type")
    assert password_type == "password"



