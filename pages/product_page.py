from .locators import ObjectPageLocators
from .base_page import BasePage


class PageObject(BasePage):

    def click_to_basket(self):
        basket = self.is_element_present(*ObjectPageLocators.BASKET_SUBMIT)
        assert basket, "basket is not find"
        basket_click = self.browser.find_element(*ObjectPageLocators.BASKET_SUBMIT).click()

    def product_name(self):
        assert self.is_element_present(*ObjectPageLocators.PRODUCT_NAME), "book price is not find"
        book_name = self.browser.find_element(*ObjectPageLocators.PRODUCT_NAME)
        return book_name.text

    def product_price(self):
        assert self.is_element_present(*ObjectPageLocators.PRODUCT_PRICE), "book price is not find"
        book_price = self.browser.find_element(*ObjectPageLocators.PRODUCT_PRICE)
        return book_price.text

    def correct_data_in_badket(self, name, price):
        assert self.is_element_present(*ObjectPageLocators.PRODUCT_NAME), "basket product name not find"
        assert self.is_element_present(*ObjectPageLocators.BASKET_PRODUCT_PRICE)
        basket_book_name = self.browser.find_element(*ObjectPageLocators.PRODUCT_NAME)
        basket_book_price = self.browser.find_element(*ObjectPageLocators.BASKET_PRODUCT_PRICE)
        assert basket_book_name.text == name, "The name of the product does not match the selected"
        assert basket_book_price.text == price, "The price of the product does not match the selected"





