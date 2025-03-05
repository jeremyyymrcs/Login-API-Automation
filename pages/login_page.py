from seleniumbase import BaseCase

from pages.base_page import BasePage
from utilities.custom_logging import get_custom_logger
from configurations.config_reader import ReadConfig
from locators.locators import LoginPageLocators

logger = get_custom_logger(__name__)


class LoginPage(BasePage):

    def login_using_totp_code(self):
        """Login using username, password, and TOTP code"""
        try:

            logger.info("Starting login test...")

            logger.info("Checking if the MFA login testing page label is visible.")
            self.assert_element(LoginPageLocators.MFA_LOGIN_TESTING_PAGE_LABEL)
            logger.info("MFA Login Testing Page label is visible.")

            logger.info("Entering username and password.")
            self.type(LoginPageLocators.USERNAME, ReadConfig.get_user_name())
            self.type(LoginPageLocators.PASSWORD, ReadConfig.get_secret_password())

            # Read the TOTP code from file
            logger.info("Reading generated totp code the saved file.")
            with open("..//data//saved_totp_code.txt", "r") as file:
                generated_totp_code = file.read().strip()
            logger.info(f"Generated secret key read: {generated_totp_code}")

            logger.info("Entering the multifactor authentication code.")
            self.type(LoginPageLocators.MULTIFACTOR_AUTH_CODE, generated_totp_code)

            logger.info("Clicking the sign-in button.")
            self.click(LoginPageLocators.SIGN_IN_BUTTON)

            logger.info("Login test completed successfully.")


        except Exception as e:

            logger.error(f"An error occurred during the login test: {e}")
            raise

    def successful_login_using_mfa_code(self):
        try:

            logger.info("Starting login test...")

            logger.info("Checking if the MFA login testing page label is visible.")
            self.assert_element(LoginPageLocators.MFA_LOGIN_TESTING_PAGE_LABEL, timeout=15)
            logger.info("MFA Login Testing Page label is visible.")

            logger.info("Entering username and password.")
            self.type(LoginPageLocators.USERNAME, ReadConfig.get_user_name())
            self.type(LoginPageLocators.PASSWORD, ReadConfig.get_secret_password())

            logger.info("Entering the multifactor authentication code.")
            self.enter_mfa_code(LoginPageLocators.MULTIFACTOR_AUTH_CODE, ReadConfig.get_secret_key())
            logger.info("Login test completed successfully.")

        except Exception as e:
            logger.error(f"An error occurred during the login test: {e}")
            raise

    def failed_login_attempt_with_incorrect_password(self):
        """Attempt login with incorrect password and verify the error message"""
        try:
            logger.info("Starting the login test with incorrect password.")

            logger.info("Checking if the MFA login page label is visible.")
            self.assert_element(LoginPageLocators.MFA_LOGIN_TESTING_PAGE_LABEL, timeout=15)
            logger.info("MFA Login Testing Page label is visible.")

            logger.info("Entering username 'demo_user' and incorrect password 'wong_password'.")
            self.type(LoginPageLocators.USERNAME, ReadConfig.get_user_name())
            self.type(LoginPageLocators.PASSWORD, ReadConfig.get_wrong_password())  # Enter the incorrect password

            # Enter the MFA code
            logger.info("Entering the multifactor authentication code")
            self.type(LoginPageLocators.MULTIFACTOR_AUTH_CODE, ReadConfig.get_secret_key())
            self.click(LoginPageLocators.SIGN_IN_BUTTON)

            # Assert that the invalid password warning appears
            logger.info("Checking for invalid password warning.")
            self.assert_element(LoginPageLocators.INVALID_PASSWORD_WARNING)
            logger.info("Invalid password warning found, as expected.")

            logger.info("Login test completed: Login attempt failed due to incorrect password.")

        except Exception as e:

            logger.error(f"An error occurred during the login test: {e}")
            raise
