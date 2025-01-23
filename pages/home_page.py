from seleniumbase import BaseCase
from utilities.custom_logging import get_custom_logger

# Set up logger
logger = get_custom_logger(__name__)


class HomePage(BaseCase):
    welcome_label = '//h1[normalize-space(text())="Welcome!"]'
    image = "#image1"

    def verify_home_page(self):
        self.sleep(2)
        logger.info("Asserting the element")
        self.assert_element(self.welcome_label, timeout=20)
