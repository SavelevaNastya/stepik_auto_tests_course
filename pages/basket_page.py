from pages.base_page import BasePage
from pages.locators import BasketPageLocators
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_MESSAGE), "Your basket is not empty!"

    def should_be_message_about_empty(self):
        MESSAGE_ABOUT_EMPTY_BASKET = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET).text
        EXPECTED_MESSAGE = BasketPageLocators.EXPECTED_MESSAGE
        assert EXPECTED_MESSAGE in MESSAGE_ABOUT_EMPTY_BASKET, "Your basket is not empty!"