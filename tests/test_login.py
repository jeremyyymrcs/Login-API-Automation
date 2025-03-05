import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage


class TestLogin(LoginPage, SignUpPage, HomePage):

    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_signup(self):
        self.get_secret_key()

    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_login_with_totp_code(self):
        self.login_using_totp_code()
        self.verify_home_page()

    @pytest.mark.run(order=3)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_successful_login(self):
        self.successful_login_using_mfa_code()
        self.verify_home_page()

    @pytest.mark.run(order=4)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_failed_login(self):
        self.failed_login_attempt_with_incorrect_password()
