from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.current_url
        assert "login" in login_link, "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        REGISTRATION_EMAIL = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        REGISTRATION_EMAIL.send_keys(email)
        REGISTRATION_PASSWORD1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        REGISTRATION_PASSWORD1.send_keys(password)
        REGISTRATION_PASSWORD2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        REGISTRATION_PASSWORD2.send_keys(password)
        REGISTER_BUTTON = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        REGISTER_BUTTON.click()

