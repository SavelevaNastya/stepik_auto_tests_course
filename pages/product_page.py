from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def should_be_add_to_cart(self):
        self.add_to_cart()
        self.should_see_message()
        self.should_be_same_price()

    def cant_see_success_message_after_adding_product_to_basket(self):
        self.add_to_cart()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSE_MESSAGE), "Success message is presented"

    def cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSE_MESSAGE), "Success message is presented"
    
    def message_disappeared_after_adding_product_to_basket(self):
        self.add_to_cart()
        assert self.is_disappeared(*ProductPageLocators.SUCCESSE_MESSAGE), "Success message is still presented"

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_same_price(self):
        CART_COST = self.browser.find_element(*ProductPageLocators.CART_COST).text
        PRODUCT_COST = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        #print(f"{CART_COST} , {PRODUCT_COST}")
        assert CART_COST == PRODUCT_COST, "The price of the cart must match the price of the item."

    def should_see_message(self):
        PRODUCT_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        PRODUCT_NAME_IN_MESSAGE = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        #print(f"{PRODUCT_NAME} , {PRODUCT_NAME_IN_MESSAGE}")
        assert PRODUCT_NAME == PRODUCT_NAME_IN_MESSAGE, "The product name in the message must match the product you actually added."
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True