class WebLocators:
    # login
    username_locator = "username"
    password_locator = "password"
    login_button_locator = "//button[@type='submit']"
    error_message_locator = "//div[2]/div[2]/div/div[1]/div[1]"
    username_alert_locator = '//form/div[1]/div/span'
    password_alert_locator = '//form/div[2]/div/span'
    required_alert = "//form/div[2]/div/span"

    # pim
    pim_link_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    employee_link_locator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'

    #delete
    delete_button_locator = "//div[9]/div/button[1]"
    alert_locator = '//div[3]/button[2]'
    search_uname = "//div[2]/input"
    search_emp_name = "//div/div[2]/div/div/input"
    search_emp_id = "//div/div[2]/div/div[2]/input"
    search_button = "//div[2]/button[2]"
    first = "//div[3]/div/div[2]/div[1]/div/div[3]"

    # add
    add_button_locator = '//div[2]/div[1]/button'
    fname_locator = "//input[@name='firstName']"
    fname_required = "//div[1]/span[text()='Required']"
    mname_locator = "//input[@name='middleName']"
    lname_locator = "//input[@name='lastName']"
    lname_required = "//div[3]/span[text()='Required']"
    emp_id_locator = "//div[2]/div/div/div[2]/input"
    error_message_emp_id = "//span[text()='Employee Id already exists']"
    toggle_locator = "//div/label/span"
    uname_locator = "//div[3]/div/div[1]/div/div[2]/input"
    pass_locator = "//div[4]/div/div[1]/div/div[2]/input"
    confirm_pass_locator = "//div[4]/div/div[2]/div/div[2]/input"
    save_button_locator = "//button[2]"
    cancel_button = "//div[2]/button[1]"
    error_message_username = "//span[text()='Username already exists']"
    username_char_limit = "//span[text()='Should be at least 5 characters']"
    password_num = "//span[text()='Your password must contain minimum 1 number']"
    password_mismatch = "//span[text()='Passwords do not match']"


    # edit - personal details
    edit_button_locator = "//div[1]/div/div[9]/div/button[2]"
    form_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div'
    first_name_locator = '//input[@placeholder="First Name"]'
    middle_name_locator = '//input[@name="middleName"]'
    last_name_locator = '//input[@name="lastName"]'
    nick_name_locator = '//div[1]/div[2]/div/div/div[2]/input'
    employee_id_locator = '//div[2]/div[1]/div/div/div[2]/input'
    empid_error_message_locator = "//div/span[text()='Employee Id already exists']"
    other_id_locator = '//div[2]/div[1]/div[2]/div/div[2]/input'
    ssn_number_locator = '//div[3]/div[1]/div/div[2]/input'
    license_number_locator = '//div[2]/div[2]/div[1]/div/div[2]/input'
    sin_number_locator = '//div[3]/div[2]/div/div[2]/input'
    nationality = "//div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i"
    marital= "//div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i"
    other = "//div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]"
    save_button_locator_1 = "//div[5]/button"
    save_button_locator_2 = "//div[2]/button"
    records_found_edit = "//div/span[text()='(1) Record Found']"

    # forgot password
    forgot_password = "//div[@class='orangehrm-login-forgot']/p"
    resetpassword_username = "//input[@name='username']"
    error = "//div[1]/div/span"
    reset_button = "//div[2]/button[2]"
    cancel_button = "//div[2]/button[1]"
    reset_link_message = "//p[text()='A reset password link has been sent to you via email.']"


