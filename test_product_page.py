from .pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)
    page.open()
    product_name = page.product_name()
    product_price = page.product_price()
    page.click_to_basket()
    page.solve_quiz_and_get_code()
    page.correct_data_in_badket(product_name, product_price)






