from .base_page import BasePage
from .locators import ProductLocators

class ProductPage(BasePage):
    def add_to_backet(self):
        self.price = self.browser.find_element(*ProductLocators.RRODUCT_PRICE).text
        self.name = self.browser.find_element(*ProductLocators.PRODUCT_NAME).text
        button = self.browser.find_element(*ProductLocators.BTN_BACKET)
        button.click()
    
    def product_in_backet(self):
        backet_name = self.browser.find_element(*ProductLocators.PRODUCT_IN_BACKET_NAME).text
        assert backet_name == self.name, "Product not in backet"

    def price_equal_backet(self):
        backet_price = self.browser.find_element(*ProductLocators.PRODUCT_IN_BACKET_PRICE).text
        assert backet_price == self.price, "Backet price is not equal with price of product"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.SUCCESS_MESSAGE), "There are success message in the page"
    
    def should_disappeared_success_message(self) :
        assert self.is_disappeared(*ProductLocators.SUCCESS_MESSAGE), "Success message is dissapeared"
