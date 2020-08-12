import time

from .pages.product_page import PageObject
import pytest


# @pytest.mark.skip
# @pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#                                   f"?promo=offer{i}" for i in range(10) if i != 7])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = PageObject(browser, link)
#     page.open()
#     product_name = page.product_name()
#     product_price = page.product_price()
#     page.click_to_basket()
#     page.solve_quiz_and_get_code()
#     page.correct_data_in_basket(product_name, product_price)

# @pytest.mark.xfail
# @pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#                                   f"?promo=offer{i}" for i in range(10)])
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = PageObject(browser, link)
    page.open()
    page.click_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = PageObject(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    # Добавляем товар в корзину Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page = PageObject(browser, link)
    page.open()
    page.click_to_basket()
    page.solve_quiz_and_get_code()
    page.is_disapperaed()
