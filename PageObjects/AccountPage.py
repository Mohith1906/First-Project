from selenium.webdriver.common.by import By


class AccountPage():
    def __init__(self, driver):
        self.driver = driver

    edit_your_account_information_option_xpath = "//a[normalize-space()='Edit your account information']"

    def display_status_edit_your_account_information_option(self):
        return self.driver.find_element(By.XPATH, self.edit_your_account_information_option_xpath).is_displayed()