import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage


class TestLogin(LoginPage, SignUpPage, HomePage):

    @pytest.mark.run(order=1)
    def test_signup_and_login_with_totp_code(self):
        self.get_secret_key()
        self.switch_to_default_window()
        self.login_using_totp_code()
        self.verify_home_page()

    @pytest.mark.run(order=2)
    def test_successful_login(self):
        self.successful_login_using_mfa_code()
        self.verify_home_page()

    @pytest.mark.run(order=3)
    def test_failed_login1(self):
        self.failed_login_attempt_with_incorrect_password()
