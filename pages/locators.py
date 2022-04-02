from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")

    CART_COST = (By.XPATH, "//div[@class='alertinner ']/p/strong") 
    PRODUCT_COST = (By.XPATH, "//div[@class='col-sm-6 product_main']//p") 

    PRODUCT_NAME = (By.CSS_SELECTOR, "li[class='active']") 
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//div[@id='messages']//strong") 