from pages.base_page import BasePage
from utilities.custom_logging import get_custom_logger
from configurations.config_reader import ReadConfig
from locators.locators import LoginPageLocators
from utilities.file_operations import FileOperations

logger = get_custom_logger(__name__)


class LoginPage(BasePage):

    def _enter_credentials(self, username, password, mfa_code=None):
        """Helper function to enter username, password, and MFA code."""
        self.assert_element(LoginPageLocators.MFA_LOGIN_TESTING_PAGE_LABEL, timeout=15)
        self.type(LoginPageLocators.USERNAME, username)
        self.type(LoginPageLocators.PASSWORD, password)
        if mfa_code:
            self.enter_mfa_code(LoginPageLocators.MULTIFACTOR_AUTH_CODE, mfa_code)
        else:
            self.type(LoginPageLocators.MULTIFACTOR_AUTH_CODE, FileOperations.read_totp_code())

    def login_using_totp_code(self):
        """Login using username, password, and TOTP code"""
        try:
            logger.info("Starting login using TOTP code.")
            self._enter_credentials(ReadConfig.get_user_name(), ReadConfig.get_secret_password(), None)
            self.click(LoginPageLocators.SIGN_IN_BUTTON)
            logger.info("Login test completed successfully.")
        except Exception as e:
            logger.error(f"An error occurred during login: {e}")
            raise

    def successful_login_using_mfa_code(self):
        """Login using MFA code."""
        try:
            logger.info("Starting login using MFA code.")
            self._enter_credentials(ReadConfig.get_user_name(), ReadConfig.get_secret_password(), ReadConfig.get_secret_key())
            logger.info("Login test completed successfully.")
        except Exception as e:
            logger.error(f"An error occurred during login: {e}")
            raise

    def failed_login_attempt_with_incorrect_password(self):
        """Attempt login with incorrect password and verify error."""
        try:
            logger.info("Starting login with incorrect password.")
            self._enter_credentials(ReadConfig.get_user_name(), ReadConfig.get_wrong_password(), ReadConfig.get_secret_key())
            self.click(LoginPageLocators.SIGN_IN_BUTTON)
            self.assert_element(LoginPageLocators.INVALID_PASSWORD_WARNING)
            logger.info("Invalid password warning found, as expected.")
        except Exception as e:
            logger.error(f"An error occurred during login: {e}")
            raise
