# Import necessary modules and classes
from Data import data
from Locators import locators
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from Automation_Scripts.add import Add


# Fixture to set up the 'Add' instance for the module
@pytest.fixture
def add_instance():
    add = Add()
    add.booting_function()
    add.login()
    yield add  # Provide the instance to the test


# Helper function to navigate to PIM and click the 'Add' button
def navigate_to_pim_and_click_add(add_instance):
    pim_link = WebDriverWait(add_instance.driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
    pim_link.click()
    click_add = WebDriverWait(add_instance.driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().add_button_locator)))
    click_add.click()


# Positive Test Cases
# Test case to validate the addition and search of an employee
def test_add_emp(add_instance):
    # Positive test case for adding an employee
    add_instance.add_emp()
    sleep(25)  # Add a sleep for the changes to take effect (modify as needed)

    # Navigate back to the PIM module
    pim_link = WebDriverWait(add_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim_link_locator)))
    pim_link.click()

    # Search for the added employee by last name and ID
    search_input = WebDriverWait(add_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_name)))
    search_input.send_keys(data.WebData().add_lname)

    search_emp_id = WebDriverWait(add_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_emp_id)))
    search_emp_id.send_keys(data.WebData().add_emp_id)
    # Introduce a brief pause
    sleep(3)

    search_button = WebDriverWait(add_instance.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().search_button)))
    search_button.click()

    sleep(15)  # Add a sleep for the search results to load (modify as needed)

    # Assert the current URL to confirm the employee is added
    assert add_instance.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    records_found_message = add_instance.driver.find_element(By.XPATH, "//div[2]/div[2]/div/span").text
    assert records_found_message == "(1) Record Found"


# Test case to check for duplicate Employee ID
def test_duplicate_employee_id_error(add_instance):
    # Add an employee to ensure there's an existing Employee ID
    # Navigate to PIM page and click Add
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)

    # Fill in the Employee ID field with an existing Employee ID
    emp_id = WebDriverWait(add_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().emp_id_locator)))
    emp_id.send_keys(Keys.CONTROL + 'a')
    emp_id.send_keys(Keys.BACKSPACE)
    emp_id.send_keys(data.WebData().add_emp_id)
    print("Employee ID filled")
    sleep(2)
    # Save the employee details
    save = WebDriverWait(add_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator)))
    save.click()

    # Check if the Employee ID is unique by checking for the error message
    error_message_emp_id = WebDriverWait(add_instance.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().error_message_emp_id)))
    assert error_message_emp_id.text == "Employee Id already exists"


# Test case to verify cancellation of employee addition
def test_add_emp_cancel(add_instance):
    # Navigate to PIM page and click 'Add'
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)

    # Click on the 'Cancel' button
    cancel = WebDriverWait(add_instance.driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().cancel_button)))
    cancel.click()
    sleep(5)

    # Assert if the current URL redirects to the employee list after canceling the addition
    assert add_instance.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"


# Negative Test cases
# Test case to check for error messages when the First Name field is empty
def test_add_emp_empty_first_name(add_instance):
    # Navigate to PIM page and click 'Add'
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)

    # Fill in the First Name field
    WebDriverWait(add_instance.driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().fname_locator))).send_keys(
        data.WebData().fname_space)
    print("First Name filled")
    sleep(5)

    # Check if the First name field is empty by checking for error messages
    error_message_fname = add_instance.driver.find_elements(By.XPATH, locators.WebLocators().fname_required)
    assert error_message_fname[0].text == "Required"


# Test case to check for error messages when the Last Name field is cleared
def test_add_emp_clear_last_name(add_instance):
    # Navigate to PIM page and click 'Add'
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)

    # Fill in the Last Name field
    lname = WebDriverWait(add_instance.driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().lname_locator)))
    lname.send_keys(data.WebData().add_lname)
    sleep(5)
    lname.send_keys(Keys.CONTROL + 'a')
    lname.send_keys(Keys.BACKSPACE)
    sleep(10)

    # Check if the Last Name field is empty by checking for error messages
    error_message_lname = add_instance.driver.find_elements(By.XPATH, locators.WebLocators().lname_required)
    assert error_message_lname[0].text == "Required"


# Test case to check for error messages when saving without entering input data
def test_add_emp_save_without_data(add_instance):
    # Navigate to PIM page and click 'Add'
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)

    # Save without entering input data into any input box
    save = WebDriverWait(add_instance.driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().save_button_locator)))
    save.click()
    sleep(5)

    # Check if the First name field is empty by checking for error messages
    error_message_fname = add_instance.driver.find_elements(By.XPATH, locators.WebLocators().fname_required)
    assert error_message_fname[0].text == "Required"

    # Check if the Last Name field is empty by checking for error messages
    error_message_lname = add_instance.driver.find_elements(By.XPATH, locators.WebLocators().lname_required)
    assert error_message_lname[0].text == "Required"


# Test case to check the character limit validation for the Username field
def test_add_username_character_limit_validation(add_instance):
    # Navigate to PIM page and click Add
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)
    # Locate and click the toggle
    toggle = WebDriverWait(add_instance.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().toggle_locator)))
    toggle.click()
    # Introduce a brief pause to allow the page to load
    sleep(2)
    # Fill in the Username field with characters violating the limit
    add_instance.driver.find_element(By.XPATH, locators.WebLocators().uname_locator).send_keys(
        data.WebData().username_char)
    print("UserName filled")
    # Check if the error message for character limit is displayed
    character_limit_error_message = add_instance.driver.find_elements(By.XPATH,
                                                                      locators.WebLocators().username_char_limit)
    assert character_limit_error_message[0].text == "Should be at least 5 characters"


# Test case to check the error message when adding an existing Username
def test_add_existing_username_error_message(add_instance):
    # Add an employee to ensure there's an existing Username
    add_instance.add_emp()
    # Navigate to PIM page and click Add
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)
    # Locate and click the toggle
    toggle = WebDriverWait(add_instance.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().toggle_locator)))
    toggle.click()
    # Introduce a brief pause to allow the page to load
    sleep(2)
    # Fill in the Username field with an existing Username
    username_field = WebDriverWait(add_instance.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().uname_locator)))
    username_field.send_keys(data.WebData().add_username)
    print("UserName filled")
    # Check if the error message for existing Username is displayed
    existing_username_error_message = add_instance.driver.find_elements(By.XPATH,
                                                                        locators.WebLocators().error_message_username)
    assert existing_username_error_message[0].text == "Username already exists"


# Test case to check the error messages when the password does not match the confirmation
def test_add_password_error_message_password_mismatch(add_instance):
    # Navigate to PIM page and click Add
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)

    # Locate and click the toggle
    toggle = WebDriverWait(add_instance.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().toggle_locator)))
    toggle.click()

    # Fill in the Password field with an invalid password
    password_field = WebDriverWait(add_instance.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pass_locator)))
    password_field.send_keys(data.WebData().password_mismatch)
    print("Password filled")

    # Fill in the Confirm Password field with a different invalid password
    add_instance.driver.find_element(By.XPATH, locators.WebLocators().confirm_pass_locator).send_keys(
        data.WebData().confirm_password_mismatch)
    print("Confirm Password filled")

    # Check if the error message for password mismatch is displayed
    password_mismatch_error_message = WebDriverWait(add_instance.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().password_mismatch)))
    assert password_mismatch_error_message.text == "Passwords do not match"


# Test case to check the error messages when the password does not contain a minimum of 1 number
def test_add_password_error_message_missing_number(add_instance):
    # Navigate to PIM page and click Add
    navigate_to_pim_and_click_add(add_instance)
    # Introduce a brief pause to allow the page to load
    sleep(3)

    # Locate and click the toggle
    toggle = WebDriverWait(add_instance.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().toggle_locator)))
    toggle.click()

    # Fill in the Password field with an invalid password missing a number
    password_field = WebDriverWait(add_instance.driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pass_locator)))
    password_field.send_keys(data.WebData().password_no_num)
    print("Password filled")

    # Check if the error message for a missing number in the password is displayed
    password_error_message = WebDriverWait(add_instance.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().password_num)))
    assert password_error_message.text == "Your password must contain minimum 1 number"
