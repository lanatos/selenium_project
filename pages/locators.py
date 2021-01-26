from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_REG = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_REG1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_REG2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REG = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductLocators():
    BTN_BACKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    RRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_IN_BACKET_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_IN_BACKET_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BACKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCTS = (By.CSS_SELECTOR, "#basket_formset")
    NOTICE_NULL = (By.CSS_SELECTOR, "#content_inner > p")