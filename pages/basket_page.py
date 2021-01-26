from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS), "There are products in the basket"

    def should_be_notice_null(self):
        assert self.is_element_present(*BasketPageLocators.NOTICE_NULL), "There are not message with not present products in the basket"
