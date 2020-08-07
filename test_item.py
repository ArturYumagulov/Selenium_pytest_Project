from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_clickable_basket(browser):
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "html/body//div[@class='col-sm-6 product_main']/form/button")))
    assert button.click() == None



