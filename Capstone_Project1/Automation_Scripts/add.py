"""
TC_PIM_01:

Test Objective: Add a new employee to the PIM Module.
Expected Result: The user should be able to add  a new employee  in the PIM and should see a message for successful employee addition.
"""
# Importing necessary modules and classes
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from Data import data
from Locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


class Add:
    # Initialize the WebDriver at the class level for reuse across methods
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    actions = ActionChains(driver)

    def booting_function(self):
        try:
            # Maximize the browser window, navigate to the application URL
            self.driver.maximize_window()
            self.driver.get(data.WebData().url)
            print("Browser started successfully.")
            return True
        except Exception as e:
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    def shutdown(self):
        # Close the browser
        self.driver.quit()

    def login(self):
        try:
            # Enter username, password, and click on the login button
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)

            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password)

            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Login successful.")
            return True
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def add_emp(self):
        try:
            # Navigate to PIM page for employee addition
            pim_link = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
            pim_link.click()
            # Click on the 'Add' button to add a new employee
            click_add = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().add_button_locator)))
            click_add.click()
            # Introduce a brief pause to allow the page to load
            sleep(2)
            # Use actions to navigate through the form by pressing TAB
            self.actions.send_keys(Keys.TAB).perform()
            # Fill in the First Name field
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().fname_locator))).send_keys(
                data.WebData().add_fname)
            print("First Name filled")
            # Fill in the Middle Name field
            self.driver.find_element(By.XPATH, locators.WebLocators().mname_locator).send_keys(data.WebData().add_mname)
            print("Middle Name filled")
            # Fill in the Last Name field
            self.driver.find_element(By.XPATH, locators.WebLocators().lname_locator).send_keys(data.WebData().add_lname)
            print("Last Name filled")
            sleep(3)
            # Fill in the Employee ID field
            emp_id = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().emp_id_locator)))
            emp_id.send_keys(Keys.CONTROL + 'a')
            emp_id.send_keys(Keys.BACKSPACE)
            emp_id.send_keys(data.WebData().add_emp_id)
            print("Employee ID filled")
            # Check if the Employee ID is unique by checking for error messages
            # Check if the Employee ID is unique by checking for error messages
            error_message_emp_id = self.driver.find_elements(By.XPATH, locators.WebLocators().error_message_emp_id)
            if error_message_emp_id:
                raise ValueError(f"Error: {error_message_emp_id[0].text}")
            # Toggle if applicable
            toggle = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().toggle_locator)))
            toggle.click()
            # Fill in the Username field
            self.driver.find_element(By.XPATH, locators.WebLocators().uname_locator).send_keys(
                data.WebData().add_username)
            print("UserName filled")

            # Fill in the Password field
            self.driver.find_element(By.XPATH, locators.WebLocators().pass_locator).send_keys(
                data.WebData().add_password)
            print("Password filled")
            # Fill in the Confirm Password field
            self.driver.find_element(By.XPATH, locators.WebLocators().confirm_pass_locator).send_keys(
                data.WebData().confirm_password)
            print("Confirm Password filled")
            sleep(2)

            # Save the employee details
            save = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator)))
            save.click()
            sleep(10)

            # Wait for the form to be visible
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().form_locator)))

            # Clear and fill other ID
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().other_id_locator))).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().other_id_locator).send_keys(
                data.WebData().other_id)
            sleep(2)

            # Clear and fill license number
            self.driver.find_element(By.XPATH, locators.WebLocators().license_number_locator).clear()
            self.driver.find_element(By.XPATH, locators.WebLocators().license_number_locator).send_keys(
                data.WebData().license_number)
            sleep(2)

            # Select nationality from dropdown
            nationality = locators.WebLocators().nationality
            n_dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, nationality)))
            n_dropdown.click()
            sleep(1)  # Add a short sleep to ensure the dropdown options are loaded

            self.driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[3]").click()
            sleep(1)
            # Select marital status from dropdown
            marital_status = locators.WebLocators().marital
            m_dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, marital_status)))
            m_dropdown.click()
            sleep(1)  # Add a short sleep to ensure the dropdown options are loaded

            self.driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[3]").click()
            sleep(1)

            # Save the changes
            save_button_1 = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator_1)))
            save_button_1.click()

            save_button_2 = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator_2)))
            save_button_2.click()
            sleep(2)

        except Exception as e:
            # Handling exceptions by printing an error message and saving a screenshot
            print(f"Error: {e}")
            self.driver.save_screenshot("error_screenshot.png")


if __name__ == "__main__":
    # Create an instance of the 'Add' class to perform employee addition
    add = Add()
    # Check if browser initialization and login are successful
    if add.booting_function() and add.login():
        # Perform Add function
        add.add_emp()
        # Print completion message
        print("Add operation completed successfully.")






