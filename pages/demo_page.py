from seleniumbase import BaseCase
from locators.locators import DemoPageLocators
from utilities.custom_logging import get_custom_logger

logger = get_custom_logger(__name__)


class DemoPage(BaseCase):

    def verify_demo_page(self):
        try:
            self.click(DemoPageLocators.DEMO_PAGE_TAB)
            self.assert_element(DemoPageLocators.DEMO_PAGE_TAB)
        except Exception as e:

            logger.error(f"An error occurred during demo page: {e}")
            raise

        # THIS IS THE CONTINUATION OF DEMO PAGE

        # THIS IS THE CONTINUATION OF DEMO PAGE2

        # THIS IS THE CONTINUATION OF DEMO PAGE3

        # THIS IS THE CONTINUATION OF DEMO PAGE4
