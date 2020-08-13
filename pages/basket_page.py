from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def go_to_basket(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_LINK_PRODUCT_PAGE)
        button.click()

    def should_be_present_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LINK_PRODUCT_PAGE), "Basket link not found"

    def should_be_wait_is_not_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET)

