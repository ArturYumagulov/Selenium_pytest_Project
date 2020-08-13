import time
from .pages.basket_page import BasketPage
from .pages.product_page import PageObject
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"



@pytest.mark.skip
# @pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#                                   f"?promo=offer{i}" for i in range(10) if i != 7])
def test_guest_can_add_product_to_basket(browser):
    page = PageObject(browser, link)
    page.open()
    product_name = page.product_name()
    product_price = page.product_price()
    page.click_to_basket()
    page.solve_quiz_and_get_code()
    page.correct_data_in_basket(product_name, product_price)


@pytest.mark.skip
# @pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#                                   f"?promo=offer{i}" for i in range(10)])
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


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    # Добавляем товар в корзину Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page = PageObject(browser, link)
    page.open()
    page.click_to_basket()
    page.solve_quiz_and_get_code()
    page.is_disapperaed()


def test_guest_should_see_login_link_on_product_page(browser):
    page = PageObject(browser, link_2)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = PageObject(browser, link_2)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает главную страницу
    page = BasketPage(browser, link)
    page.open()
    page.should_be_present_basket()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket()
    page.should_be_wait_is_not_product_in_basket()
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
