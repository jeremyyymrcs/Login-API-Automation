import pytest
from seleniumbase import BaseCase
from utilities.custom_logging import get_custom_logger
from configurations.config_reader import ReadConfig

logger = get_custom_logger(__name__)


class BasePage(BaseCase):

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Fixture to run before and after each test."""
        print("\n\n=== Starting New Test Case ===")
        logger.info("Setting up the browser and opening the website.")

        try:
            super().setUp()
            self.open_website()
        except Exception as e:
            logger.error(f"Error during setup: {e}")
            raise e

        yield

        try:
            print("=== Test Case Completed ===\n")
        finally:
            super().tearDown()  # Ensures BaseCase's tearDown() is executed

    def open_website(self):
        """Open the login page by reading the URL from the configuration file."""
        login_url = ReadConfig.get_mfa_login_url()
        logger.info(f"Opening the login page: {login_url}")

        try:
            super().open(login_url)
            logger.info("Webpage opened successfully.")
        except Exception as e:
            logger.error(f"Error opening the webpage: {e}")
            raise e
