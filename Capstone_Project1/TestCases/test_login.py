"""
TC_Login_01 Automation Script:

Description: This automation script is designed to verify the successful login functionality of the OrangeHRM portal for employees.
Steps:
Launch the OrangeHRM portal.
Enter valid employee credentials.
Click on the login button.
Expected Outcome: The script expects the user to be logged in successfully, indicating that the login functionality is working as expected.

TC_Login_02 Automation Script:

Description: This automation script aims to validate the handling of invalid login attempts on the OrangeHRM portal for employees.
Steps:
Launch the OrangeHRM portal.
Enter invalid employee credentials.
Click on the login button.
Expected Outcome: The script anticipates the display of a valid error message indicating that the provided credentials are invalid, thus ensuring proper error-handling functionality.
"""

# Import necessary modules and classes
import pytest
from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Orange_HRM:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(data.WebData().url)
        assert self.driver.title == data.WebData().homepage_title
        print("SUCCESS: Web Title Verified")

    def test_login_valid_credentials(self, booting_function):
        self.driver.get(data.WebData().url)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
            data.WebData().username)
        self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
            data.WebData().password)
        self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
        assert self.driver.current_url == data.WebData().dashboard_url

    def test_login_invalid_password(self, booting_function):
        self.driver.get(data.WebData().url)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
            data.WebData().username)
        self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
            data.WebData().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().error_message_locator)))
        # assert self.driver.current_url == data.WebData().dashboard_url
        assert error_message_element.is_displayed()
        assert error_message_element.text == "Invalid credentials"

    def test_login_invalid_credentials_positive(self, booting_function):
        self.driver.get(data.WebData().url)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
            data.WebData().invalid_username)
        self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
            data.WebData().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().error_message_locator)))
        # assert self.driver.current_url == data.WebData().dashboard_url
        assert error_message_element.is_displayed()
        assert error_message_element.text == "Invalid credentials"

    def test_login_invalid_credentials_negative(self, booting_function):
        self.driver.get(data.WebData().url)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
            data.WebData().invalid_username)
        self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
            data.WebData().invalid_password)
        self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().error_message_locator)))
        # assert self.driver.current_url == data.WebData().dashboard_url
        assert error_message_element.is_displayed()
        assert error_message_element.text == "Please enter valid credentials"

    def test_login_empty_credentials_positive(self, booting_function):
        self.driver.get(data.WebData().url)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
            data.WebData().empty_username)
        self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
            data.WebData().empty_password)
        self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

        username_alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().username_alert_locator)))
        assert username_alert.is_displayed()
        assert username_alert.text == "Required"

        password_alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().password_alert_locator)))
        assert password_alert.is_displayed()
        assert password_alert.text == "Required"

    def test_login_empty_credentials_negative(self, booting_function):
        self.driver.get(data.WebData().url)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
            data.WebData().empty_username)
        self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
            data.WebData().empty_password)
        self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

        error_message_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().required_alert)))
        # assert self.driver.current_url == data.WebData().dashboard_url
        assert error_message_element.is_displayed()
        assert error_message_element.text == "Invalid Credentials"
