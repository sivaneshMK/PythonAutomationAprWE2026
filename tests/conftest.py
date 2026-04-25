import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    return driver

@pytest.fixture(scope ='function')
def get_driver1():
    driver = webdriver.Chrome()
    driver.get("https://www.foundit.in/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope ='function')
def get_driver2():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://beej.us/blog/data/drag-n-drop/")
    driver.maximize_window()
    yield driver
    driver.quit()

