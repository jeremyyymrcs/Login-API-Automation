from seleniumbase import BaseCase
from utilities.custom_logging import get_custom_logger
from configurations.config_reader import ReadConfig

logger = get_custom_logger(__name__)


class BasePage(BaseCase):

    def setUp(self):
        """This is automatically run by SeleniumBase before each test"""
        print("\n\n=== Starting New Test Case ===")
        logger.info(f"Setting up the browser and opening the website.")
        super().setUp()
        self.open_website()

    def tearDown(self):
        # This is automatically run by SeleniumBase after each test
        print("=== Test Case Completed ===\n")
        super().tearDown()

    def open_website(self):
        """Open the login page by reading the URL from the configuration file"""
        logger.info("Opening the login website.")
        self.open(ReadConfig.get_mfa_login_url())
        logger.info("Webpage already opened")
