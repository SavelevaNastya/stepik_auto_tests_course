from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTRATION_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "input[name='registration-password2']")

    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")

    CART_COST = (By.XPATH, "//div[@class='alertinner ']/p/strong") 
    PRODUCT_COST = (By.XPATH, "//div[@class='col-sm-6 product_main']//p") 

    PRODUCT_NAME = (By.CSS_SELECTOR, "li[class='active']") 
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//div[@id='messages']//strong") 

    SUCCESSE_MESSAGE = (By.XPATH, "//div[@id='messages']/div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_ABOUT_EMPTY_BASKET = (By.XPATH, '//p')
    EXPECTED_MESSAGE = "Your basket is empty."
    
    NOT_EMPTY_MESSAGE = (By.XPATH, "//h2[@class]")
