"""
TC_PIM_02 Test Script:

Description: This automation script aims to validate the functionality of editing an existing employee's information in the PIM (Personnel Information Management) module of the system.
Steps:
Access the PIM module of the system.
Select the employee's record.
Update the relevant details for the employee, such as contact information, position, or any other necessary fields.
Save the changes.
Expected Outcome: The automation script expects the user to successfully edit the existing employee's information in the PIM module.
"""

# Importing necessary modules and classes
import pytest
from Data import data
from Locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from Automation_Scripts.edit import Edit

# Fixture to set up the 'Edit' instance for the module
@pytest.fixture
def edit_instance():
    # Setup the edit instance for the module
    edit = Edit()
    edit.booting_function()
    edit.login()
    yield edit  # Provide the instance to the test


# Positive test case for editing an employee
def test_edit_emp_positive(edit_instance):
    edit_instance.edit_emp()
    sleep(25)

    # Navigate back to the PIM module
    pim_link = WebDriverWait(edit_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
    pim_link.click()

    # Search the edited employee by name
    search_emp_name = WebDriverWait(edit_instance.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name))
    )
    search_emp_name.send_keys(data.WebData.last_name)

    # Search the edited employee by ID
    search_emp_id = WebDriverWait(edit_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_id))
    )
    search_emp_id.send_keys(data.WebData.employee_id)
    sleep(3)

    # Click on the search button
    search_button = WebDriverWait(edit_instance.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button))
    )
    search_button.click()

    sleep(15)


    record_found_message = WebDriverWait(edit_instance.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().records_found_edit)))

    # Assert the current URL to confirm the employee is edited
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    assert edit_instance.driver.current_url == expected_url

    assert record_found_message.text == "(1) Record Found"


# Helper function to edit an employee with an existing ID and get the error message
def edit_employee_with_existing_id_and_get_error_message(edit_instance):
    # Navigate to the PIM page
    pim_link = WebDriverWait(edit_instance.driver, 1).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
    pim_link.click()

    # Retrieve the name of the employee in the first row
    name_in_first_row = WebDriverWait(edit_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().first))).text
    print(f"Name of the employee in the first row: {name_in_first_row}")

    # Edit the employee using the edit button
    edit_button = WebDriverWait(edit_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().edit_button_locator)))
    edit_button.click()

    # Provide an existing employee ID and trigger an error
    emp_id = WebDriverWait(edit_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().employee_id_locator)))
    emp_id.send_keys(Keys.CONTROL + 'a')
    emp_id.send_keys(Keys.BACKSPACE)
    emp_id.send_keys(data.WebData().employee_id)
    sleep(10)


# Negative test case for editing an employee with an existing ID
def test_edit_emp_negative_existing_id(edit_instance):
    # Edit an employee with an existing ID and get the error message
    edit_employee_with_existing_id_and_get_error_message(edit_instance)
    # Check for the error message and print it
    error_message = WebDriverWait(edit_instance.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().empid_error_message_locator))).text
    print(f"Error Message: {error_message}")

    # Assert that the error message is as expected
    assert error_message == "Employee Id already exists"


# Another negative test case for editing an employee with an existing ID
def test_edit_emp_negative_existing_id_2(edit_instance):
    # Edit an employee with an existing ID and get the error message
    edit_employee_with_existing_id_and_get_error_message(edit_instance)
    # Check for the error message and print it
    error_message = WebDriverWait(edit_instance.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().empid_error_message_locator))).text
    print(f"Error Message: {error_message}")

    # Assert that the error message is empty
    assert error_message == ""
