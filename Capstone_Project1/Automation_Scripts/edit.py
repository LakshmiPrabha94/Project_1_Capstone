# Importing necessary modules and classes
from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Edit:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    actions = ActionChains(driver)

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
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))
            ).send_keys(data.WebData().username)

            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password)

            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Login successful.")
            return True
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def wait_and_send_keys(self, locator, value):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(value)

    def edit_emp(self):
        try:
            # Navigation to edit page
            for locator in [
                locators.WebLocators().pim_link_locator,
                locators.WebLocators().employee_link_locator,
                locators.WebLocators().edit_button_locator,
            ]:
                WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, locator))
                ).click()

            print("Employee List is loaded.")
            sleep(3)

            # Editing employee details
            fields_to_edit = {
                locators.WebLocators().first_name_locator: data.WebData().first_name,
                locators.WebLocators().middle_name_locator: data.WebData().middle_name,
                locators.WebLocators().last_name_locator: data.WebData().last_name,
                #locators.WebLocators().nick_name_locator: data.WebData().nick_name,
                locators.WebLocators().employee_id_locator: data.WebData().employee_id,
                locators.WebLocators().other_id_locator: data.WebData().other_id,
                locators.WebLocators().ssn_number_locator: data.WebData().ssn_number,
                locators.WebLocators().license_number_locator: data.WebData().license_number,
                locators.WebLocators().sin_number_locator: data.WebData().sin_number
            }

            for locator, value in fields_to_edit.items():
                self.wait_and_send_keys(locator, value)
                sleep(2)

            # Save the changes
            for save_button_locator in [
                locators.WebLocators().save_button_locator_1,
                locators.WebLocators().save_button_locator_2
            ]:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, save_button_locator))
                ).click()
                sleep(2)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    edit = Edit()
    if edit.booting_function() and edit.login():
        edit.edit_emp()
        # Print completion message
        print("Edit operation completed successfully.")

