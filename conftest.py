import pytest
import time
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ")


@pytest.fixture()
def browser(request):
    browser_language = request.config.getoption('language')
    browser = webdriver.Chrome()
    browser.get(f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/")
    yield browser
    browser.quit()
