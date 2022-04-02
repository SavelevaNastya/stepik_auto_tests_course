from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_cart(self):
        self.add_to_cart()
        self.solve_quiz_and_get_code()
        self.should_see_message()
        self.should_be_same_price()

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
