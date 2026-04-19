import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    return driver

