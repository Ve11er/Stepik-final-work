from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_name_in_cart_correct(self):
        product_name_on_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME).text
        assert product_name_in_cart == product_name_on_product_page, \
            "Product name is not same with product name in cart"

    def product_price_in_cart_correct(self):
        product_price_on_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME).text
        assert product_price_in_cart == product_price_on_product_page, \
            "Product price is not same with product price in cart"

    def click_add_to_cart_button(self):
        add_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_cart_button.click()

