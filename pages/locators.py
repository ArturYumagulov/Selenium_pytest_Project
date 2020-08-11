from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_LINK = (By.CSS_SELECTOR, "#register_form")


class ObjectPageLocators:
    BASKET_SUBMIT = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
