from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    # Use a CSS selector that matches the bootstrap danger alert
    Warning_message_css_selector = "div.alert.alert-danger.alert-dismissible"

    def enter_email_address_field(self,email_address_text):
        self.driver.find_element(By.ID, self.email_address_field_id).click()
        self.driver.find_element(By.ID, self.email_address_field_id).clear()
        self.driver.find_element(By.ID,self.email_address_field_id).send_keys(email_address_text)

    def enter_password_field(self,password_text):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def click_on_login_button_after_credentials(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def retrieve_warning_message(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, self.Warning_message_css_selector).text
        except NoSuchElementException:
            # Return empty string if the warning isn't present to avoid throwing from tests
            return ""
