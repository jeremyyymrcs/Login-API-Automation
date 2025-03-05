from seleniumbase import BaseCase

from locators.locators import HomePageLocators
from utilities.custom_logging import get_custom_logger

# Set up logger
logger = get_custom_logger(__name__)


class HomePage(BaseCase):

    def verify_home_page(self):
        try:
            self.sleep(2)
            self.assert_element(HomePageLocators.WELCOME_LABEL)
        except Exception as e:

            logger.error(f"An error occurred during verifying home page: {e}")
            raise
