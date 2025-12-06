import pytest
from datetime import datetime
from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage
from PageObjects.AccountPage import AccountPage
from PageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_login_button()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address_field("mohithv47@gmail.com")
        login_page.enter_password_field("12345")
        login_page.click_on_login_button_after_credentials()
        account_page = AccountPage(self.driver)
        assert account_page.display_status_edit_your_account_information_option()

    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_login_button()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address_field(self.generate_email_with_time_stamp())
        login_page.enter_password_field("12345")
        login_page.click_on_login_button_after_credentials()
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message() == expected_message

    def test_Login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_login_button()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address_field("mohithv47@gmail.com")
        login_page.enter_password_field("123426735")
        login_page.click_on_login_button_after_credentials()
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message() == expected_message

    def test_Login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_login_button()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address_field("")
        login_page.enter_password_field("")
        login_page.click_on_login_button_after_credentials()
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message() == expected_message

    def generate_email_with_time_stamp(self):
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        return "mohithv47" + timestamp + "@gmail.com"