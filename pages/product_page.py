from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def item_name_in_basket_correct(self):
        item_name_on_product_page = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_name_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_ACC_PAGE).text
        assert item_name_on_product_page == item_name_in_basket, f"You have an error on {self.browser.current_url}"

    def item_prize_in_basket_correct(self):
        item_prize_on_product_page = self.browser.find_element(*ProductPageLocators.ITEM_PRIZE).text
        item_prize_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_PRIZE_ACC_PAGE).text
        assert item_prize_in_basket == item_prize_on_product_page, f"Prizes in basket and on product page" \
                                                                   f" are not the same"

    def click_add_to_basket_button(self):
        find_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        find_button.click()

    def cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message isn't disappeared."

    def cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
