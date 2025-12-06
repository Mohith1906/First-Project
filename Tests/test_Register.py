import pytest
from selenium.webdriver.common.by import By
from datetime import datetime

from PageObjects.HomePage import HomePage
from PageObjects.AccountSuccessPage import AccountSuccessPage
from PageObjects.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_register_button()
        register_page = RegisterPage(self.driver)
        register_page.enter_firstname("Mohith")
        register_page.enter_lastname("V")
        register_page.enter_email(self.generate_email_with_time_stamp())
        register_page.enter_telephone("1234567890")
        register_page.enter_password("12345")
        register_page.enter_confirm_password("12345")
        register_page.check_box_to_agree()
        register_page.click_on_continue()
        expected_heading_text = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.retrieve_account_creation_message() == expected_heading_text

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_register_button()
        register_page = RegisterPage(self.driver)
        register_page.enter_firstname("Mohith")
        register_page.enter_lastname("V")
        register_page.enter_email(self.generate_email_with_time_stamp())
        register_page.enter_telephone("1234567890")
        register_page.enter_password("12345")
        register_page.enter_confirm_password("12345")
        register_page.newsletter_yes_radio_button()
        register_page.check_box_to_agree()
        register_page.click_on_continue()
        expected_heading_text = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.retrieve_account_creation_message() == expected_heading_text


    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_register_button()
        register_page = RegisterPage(self.driver)
        register_page.enter_firstname("Mohith")
        register_page.enter_lastname("V")
        register_page.enter_email("mohithv47@gmail.com")
        register_page.enter_telephone("9876512345")
        register_page.enter_password("12345")
        register_page.enter_confirm_password("12345")
        register_page.newsletter_yes_radio_button()
        register_page.check_box_to_agree()
        register_page.click_on_continue()
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning() == expected_warning_message



    def test_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_register_button()
        register_page = RegisterPage(self.driver)
        register_page.enter_firstname("")
        register_page.enter_lastname("")
        register_page.enter_email("")
        register_page.enter_telephone("")
        register_page.enter_password("")
        register_page.enter_confirm_password("")
        register_page.click_on_continue()
        expected_privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_policy_warning() == expected_privacy_policy_warning_message
        expected_first_name_warning_message = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_firstname_warning() == expected_first_name_warning_message
        expected_Last_name_warning_message = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_lastname_warning() == expected_Last_name_warning_message
        expected_Email_warning_message = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_email_warning() == expected_Email_warning_message
        expected_Telephone_warning_message = "Telephone must be between 3 and 32 characters!"
        assert register_page.retrieve_telephone_warning() == expected_Telephone_warning_message
        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_password_warning() == expected_password_warning_message


    def generate_email_with_time_stamp(self):
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        return "mohithv47"+timestamp+"@gmail.com"
