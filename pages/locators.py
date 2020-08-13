from selenium.webdriver.common.by import By


class BasketPageLocators:
    BASKET_LINK_PRODUCT_PAGE = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > "
                                                 "div.basket-mini.pull-right.hidden-xs > span > a")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")


class ObjectPageLocators:
    BASKET_SUBMIT = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main']>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main']>p")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR,
                           "div #messages div[class='alert alert-safe alert-noicon alert-success  fade in'] strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR,
                            "div[id=messages] "
                            "div[class='alert alert-safe alert-noicon alert-info  fade in'] div strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
