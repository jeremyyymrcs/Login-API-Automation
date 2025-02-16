from seleniumbase import BaseCase

from pages.base_page import BasePage
from utilities.custom_logging import get_custom_logger

# Set up logger
logger = get_custom_logger(__name__)


class SignUpPage(BasePage):
    toptp_code = "//*[(contains(@id, 'totp'))]"
    sign_up_redirection = "//a[contains(.,'seleniumbase.io/realworld/signup')]"

    def get_secret_key(self):
        self.click(self.sign_up_redirection)
        self.switch_to_window(1)
        logger.info("Redirected to the sign up page.")

        logger.info("Attempting to retrieve the secret key from the page.")

        try:
            # Get the secret key from the page
            generated_totp_code = self.get_text_content(self.toptp_code, timeout=10)
            logger.info(f"Secret key retrieved successfully: {generated_totp_code}")

            # Save the secret key to a file
            with open("..//data//saved_totp_code.txt", "w") as file:
                file.write(generated_totp_code)
            logger.info("TOTP code saved to 'saved_totp_code.txt'.")

        except Exception as e:
            logger.error(f"Failed to retrieve or save the secret key: {e}")
