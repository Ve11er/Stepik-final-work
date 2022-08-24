from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM), "We have item in the busket. This is not correct."

    def basket_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Your basket is empty"
