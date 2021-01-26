import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = MAIN_PAGE
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        lp = LoginPage(browser, link)
        lp.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    bp = BasketPage(browser, link)
    bp.should_not_be_products()
    bp.should_be_notice_null()


