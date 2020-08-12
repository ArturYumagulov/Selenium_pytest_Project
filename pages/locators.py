from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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
