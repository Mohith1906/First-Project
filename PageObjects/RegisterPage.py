from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    enter_firstname_id = "input-firstname"
    enter_lastname_id = "input-lastname"
    enter_email_id = "input-email"
    enter_telephone_id = "input-telephone"
    enter_password_id = "input-password"
    enter_confirm_password_id = "input-confirm"
    click_on_checkbox_to_agree_name ="agree"
    click_on_continue_xpath = "//input[@value='Continue']"
    Newsletter_yes_radio_button_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_message_css_selector = "div.alert.alert-danger.alert-dismissible"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    firstname_field_warning_xpath = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    lastname_field_warning_xpath = "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    email_warning_xpath = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    telephone_warning = "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    password_warning = "//div[contains(text(),'Password must be between 4 and 20 characters!')]"



    def enter_firstname(self,first_name_text):
        self.driver.find_element(By.ID, self.enter_firstname_id).click()
        self.driver.find_element(By.ID, self.enter_firstname_id).clear()
        self.driver.find_element(By.ID, self.enter_firstname_id).send_keys(first_name_text)

    def enter_lastname(self,last_name_text):
        self.driver.find_element(By.ID, self.enter_lastname_id).click()
        self.driver.find_element(By.ID, self.enter_lastname_id).clear()
        self.driver.find_element(By.ID, self.enter_lastname_id).send_keys(last_name_text)

    def enter_email(self,email_text):
        self.driver.find_element(By.ID, self.enter_email_id).click()
        self.driver.find_element(By.ID, self.enter_email_id).clear()
        self.driver.find_element(By.ID, self.enter_email_id).send_keys(email_text)

    def enter_telephone(self,telephone_text):
        self.driver.find_element(By.ID, self.enter_telephone_id).click()
        self.driver.find_element(By.ID, self.enter_telephone_id).clear()
        self.driver.find_element(By.ID, self.enter_telephone_id).send_keys(telephone_text)

    def enter_password(self,password_text):
        self.driver.find_element(By.ID, self.enter_password_id).click()
        self.driver.find_element(By.ID, self.enter_password_id).clear()
        self.driver.find_element(By.ID, self.enter_password_id).send_keys(password_text)

    def enter_confirm_password(self,confirm_password_text):
        self.driver.find_element(By.ID, self.enter_confirm_password_id).click()
        self.driver.find_element(By.ID, self.enter_confirm_password_id).clear()
        self.driver.find_element(By.ID, self.enter_confirm_password_id).send_keys(confirm_password_text)


    def check_box_to_agree(self):
        self.driver.find_element(By.NAME, self.click_on_checkbox_to_agree_name).click()

    def click_on_continue(self):
        self.driver.find_element(By.XPATH, self.click_on_continue_xpath).click()

    def newsletter_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.Newsletter_yes_radio_button_xpath).click()

    def retrieve_duplicate_email_warning(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.duplicate_email_warning_message_css_selector).text

    def retrieve_privacy_policy_warning(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text

    def retrieve_firstname_warning(self):
        return self.driver.find_element(By.XPATH, self.firstname_field_warning_xpath).text

    def retrieve_lastname_warning(self):
        return self.driver.find_element(By.XPATH, self.lastname_field_warning_xpath).text

    def retrieve_email_warning(self):
        return self.driver.find_element(By.XPATH, self.email_warning_xpath).text

    def retrieve_telephone_warning(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning).text

    def retrieve_password_warning(self):
        return self.driver.find_element(By.XPATH, self.password_warning).text
