from .locators import ObjectPageLocators
from .base_page import BasePage


class PageObject(BasePage):

    def click_to_basket(self):
        basket = self.is_element_present(*ObjectPageLocators.BASKET_SUBMIT)
        assert basket, "basket is not find"
        basket_click = self.browser.find_element(*ObjectPageLocators.BASKET_SUBMIT).click()

