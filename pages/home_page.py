from seleniumbase import BaseCase
from utilities.custom_logging import get_custom_logger

# Set up logger
logger = get_custom_logger(__name__)


class HomePage(BaseCase):
    welcome_label = "//h1[contains(.,'Welcome!')]"

    def verify_home_page(self):
        self.assert_element(self.welcome_label)
