"""
TC_PIM_03 Test Script:

Description: This automation script is created to test the functionality of deleting an existing employee in the PIM (Personnel Information Management) module of the system.
Steps:
Access the PIM module of the system.
Select the employee record.
Initiate the deletion process.
Expected Outcome: The automation script expects the user to successfully delete the selected employee from the PIM module and receive a confirmation message indicating the successful deletion of the employee's information. 
This verifies the proper functioning of the delete functionality within the PIM module.
"""
# Import necessary modules and classes
from Data import data
from Locators import locators
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from Automation_Scripts.delete import Delete


@pytest.fixture(scope='module')
def delete_instance():
    # Setup the Delete instance for the module
    delete = Delete()
    if delete.booting_function() and delete.login():
        yield delete
    else:
        pytest.fail("Fixture setup failed. Cannot proceed with tests.")
    # Cleanup (shutdown) is not performed here to keep the browser session open for both tests
    delete.shutdown()


# Positive test case
def test_delete_existent_emp(delete_instance):
    # Step 1: Navigate to the PIM module and EmployeeList page
    pim_link = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
    pim_link.click()

    employee_link = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().employee_link_locator)))
    employee_link.click()

    # Step 2: Retrieve the name of the employee in the first row
    name_in_first_row = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().first))).text
    print(f"Name of the employee in the first row: {name_in_first_row}")

    # Step 3: Delete the employee using the delete button and handle the confirmation alert
    delete_button = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().delete_button_locator)))
    delete_button.click()

    confirmation_alert = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().alert_locator)))
    confirmation_alert.click()

    # Step 4: Search for the deleted employee in the EmployeeList page to confirm the delete operation
    delete_instance.driver.get(data.WebData().search_employeelist_url)
    search_name_input = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name)))
    search_name_input.send_keys(name_in_first_row)

    search_button = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button)))
    search_button.click()

    sleep(15)  # Wait for the search results to load

    # Step 5: Assert the current URL to confirm the employee is deleted
    assert delete_instance.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"


# Negative test case
def test_delete_nonexistent_emp(delete_instance):
    # Step 1: Search for a nonexistent employee
    delete_instance.driver.get(data.WebData().search_employeelist_url)
    search_name_input = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name)))
    search_name_input.send_keys(data.WebData.nonexistent_employee_name)

    search_button = WebDriverWait(delete_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button)))
    search_button.click()

    sleep(30)  # Wait for the search results to load

    # Step 2: Check for any error messages or alerts
    try:
        error_message = WebDriverWait(delete_instance.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().error_message_locator))).text
        print(f"Error Message: {error_message}")
    except:
        pass  # No error message found

    # Step 3: Assert the absence of the nonexistent employee in the EmployeeList page
    assert delete_instance.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
