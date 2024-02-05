# Import necessary modules and classes
from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    # Initialize the WebDriver at the class level for reuse across methods
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def booting_function(self):
        try:
            # Maximize the browser window and navigate to the application URL
            self.driver.maximize_window()
            self.driver.get(data.WebData().url)
            print("Browser started successfully.")
        except Exception as e:
            print(f"ERROR: Unable to start the browser: {e}")

    def shutdown(self):
        # Close the browser
        self.driver.quit()

    def login(self):
        try:
            # Wait for the username field to be visible, then enter the username
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)
            print("Entering username:", data.WebData().username)

            # Enter the password in the password field
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password)
            print("Entering password:", data.WebData().password)

            # Click on the login button
            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Clicking the login button")

            # Display a welcome message upon successful login
            print("Welcome to OrangeHRM!!!")

        except NoSuchElementException as e:
            # Handle the exception and print an error message
            print("Error : ", e)
        finally:
            # Add a brief pause before shutting down the browser
            sleep(3)
            # Close the browser
            self.shutdown()


if __name__ == '__main__':
    # Instantiate the 'Login' class to execute the login operation.
    login_page = Login()
    # Execute the 'booting_function' method to open the browser and navigate to the application URL
    login_page.booting_function()
    # Execute the 'login' method to perform the login operation
    login_page.login()
