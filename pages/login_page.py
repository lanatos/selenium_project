import re
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        str_match = r"^http://selenium1py\.pythonanywhere\.com/[a-z]{2}(-[a-z]{2})?/accounts/login/$"
        assert re.search(str_match, self.browser.current_url), "Login URL is invalid"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"
    
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_REG).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REG1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REG2).send_keys(password)
        btn_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        btn_registration.click()