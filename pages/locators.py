from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[name='login-username']")
    PASSWORD_FORM = (By.CSS_SELECTOR, "[name='login-password']")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages >div:nth-child(1)>.alertinner>strong")
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages >div:nth-child(3)>.alertinner>p>strong")
    SUCCESS_ADD_TO_CART_MSG = (By.CSS_SELECTOR, ".alert-success")
