from pages.product_page import ProductPage
import math
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.product_name_in_cart_correct()
    page.product_price_in_cart_correct()
