import time

from .pages.product_page import PageObject
import pytest


@pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                  f"?promo=offer{i}" for i in range(10) if i != 7])
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObject(browser, link)
    page.open()
    product_name = page.product_name()
    product_price = page.product_price()
    page.click_to_basket()
    page.solve_quiz_and_get_code()
    page.correct_data_in_basket(product_name, product_price)
