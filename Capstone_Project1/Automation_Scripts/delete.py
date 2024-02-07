"""
TC_PIM_03:
Test Objective: Delete an existing employee in the PIM Module.
Expected Result: The user should be able to delete existing employee information in the PIM and should see a message for successful deletion.
"""
# Importing necessary modules and classes
from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Delete:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.WebData().url)
            print("Browser started successfully.")
            return True
        except Exception as e:
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    def shutdown(self):
        self.driver.quit()

    def login(self):
        try:
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

    def delete_employee(self):
        try:
            # Navigate to the PIM module
            pim_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
            pim_link.click()

            # Navigate to the EmployeeList page
            employee_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().employee_link_locator)))
            employee_link.click()

            # Retrieve the name of the employee in the first row
            name_in_first_row = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().first))).text
            print(name_in_first_row)

            # Delete the employee using the delete button and handle the confirmation alert
            delete = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().delete_button_locator)))
            delete.click()

            alert_1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().alert_locator)))
            alert_1.click()

        except Exception as e:
            print(f"Error during deleting employee: {e}")

        # finally:
        #     # Close the browser
        #     self.shutdown()


if __name__ == "__main__":
    # Create an instance of the Delete class
    delete = Delete()
    # Start the browser and navigate to the application URL
    if delete.booting_function() and delete.login():
        # Perform Delete function
        delete.delete_employee()
        # Print completion message
        print("Delete operation completed successfully.")
