import pytest
import time
import random
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.add_backet_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #linkreg = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, MAIN_PAGE)
        page.open()
        page.go_to_login_page()
        lp = LoginPage(browser, MAIN_PAGE)
        email = str(time.time()) + "@something.com"
        password = str(random.randint(1e8, 1e9))
        lp.register_new_user(email, password)
        lp.should_be_authorized_user()
        self.link = PRODUCT_LINK
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)  
        page.open()                      
        page.should_not_be_success_message()          
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)  
        page.open()                      
        page.add_to_backet()          
        page.solve_quiz_and_get_code()
        page.product_in_backet()
        page.price_equal_backet()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_LINK)  
    page.open()                      
    page.should_not_be_success_message()          

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)  
    page.open()                      
    page.add_to_backet()          
    page.solve_quiz_and_get_code()
    page.product_in_backet()
    page.price_equal_backet()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)  
    page.open()                      
    page.add_to_backet()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message() 

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)  
    page.open()                      
    page.add_to_backet()
    page.solve_quiz_and_get_code()
    page.should_disappeared_success_message() 

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_basket_page()
    bp = BasketPage(browser, PRODUCT_LINK)
    bp.should_not_be_products()
    bp.should_be_notice_null()