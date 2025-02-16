from seleniumbase import BaseCase

from pages.base_page import BasePage
from utilities.custom_logging import get_custom_logger
from configurations.config_reader import ReadConfig

logger = get_custom_logger(__name__)


class LoginPage(BasePage):
    # Locators for the login page elements
    mfa_login_testing_page_label = "//h4[contains(.,'MFA Login Testing Page')]"
    username = "//input[@id='username']"
    password = "//input[@id='password']"
    multifactor_auth_code = "//input[contains(@placeholder,'Enter the 6-digit MFA Code')]"
    sign_in_button = "//a[@id='log-in']"
    invalid_password_warning = "//h6[contains(.,'Invalid Password!')]"

    def login_using_totp_code(self):
        """Login using username, password, and TOTP code"""
        try:

            logger.info("Starting login test...")

            logger.info("Checking if the MFA login testing page label is visible.")
            self.assert_element(self.mfa_login_testing_page_label)
            logger.info("MFA Login Testing Page label is visible.")

            logger.info("Entering username and password.")
            self.type(self.username, ReadConfig.get_user_name())
            self.type(self.password, ReadConfig.get_secret_password())

            # Read the TOTP code from file
            logger.info("Reading generated totp code the saved file.")
            with open("..//data//saved_totp_code.txt", "r") as file:
                generated_totp_code = file.read().strip()
            logger.info(f"Generated secret key read: {generated_totp_code}")

            logger.info("Entering the multifactor authentication code.")
            self.type(self.multifactor_auth_code, generated_totp_code)

            logger.info("Clicking the sign-in button.")
            self.click(self.sign_in_button)

            logger.info("Login test completed successfully.")


        except Exception as e:

            logger.error(f"An error occurred during the login test: {e}")
            raise

    def successful_login_using_mfa_code(self):
        try:

            logger.info("Starting login test...")

            logger.info("Checking if the MFA login testing page label is visible.")
            self.assert_element(self.mfa_login_testing_page_label, timeout=15)
            logger.info("MFA Login Testing Page label is visible.")

            logger.info("Entering username and password.")
            self.type(self.username, ReadConfig.get_user_name())
            self.type(self.password, ReadConfig.get_secret_password())

            logger.info("Entering the multifactor authentication code.")
            self.enter_mfa_code(self.multifactor_auth_code, ReadConfig.get_secret_key())
            logger.info("Login test completed successfully.")

        except Exception as e:
            logger.error(f"An error occurred during the login test: {e}")
            raise

    def failed_login_attempt_with_incorrect_password(self):
        """Attempt login with incorrect password and verify the error message"""
        try:
            logger.info("Starting the login test with incorrect password.")

            logger.info("Checking if the MFA login page label is visible.")
            self.assert_element(self.mfa_login_testing_page_label, timeout=15)
            logger.info("MFA Login Testing Page label is visible.")

            logger.info("Entering username 'demo_user' and incorrect password 'wong_password'.")
            self.type(self.username, ReadConfig.get_user_name())
            self.type(self.password, ReadConfig.get_wrong_password())  # Enter the incorrect password

            # Enter the MFA code
            logger.info("Entering the multifactor authentication code")
            self.type(self.multifactor_auth_code, ReadConfig.get_secret_key())
            self.click(self.sign_in_button)

            # Assert that the invalid password warning appears
            logger.info("Checking for invalid password warning.")
            self.assert_element(self.invalid_password_warning)
            logger.info("Invalid password warning found, as expected.")

            logger.info("Login test completed: Login attempt failed due to incorrect password.")

        except Exception as e:

            logger.error(f"An error occurred during the login test: {e}")
            raise
