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
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://beej.us/blog/data/drag-n-drop/")
    #driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def get_driver3():
    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.guvi.in/mlp/zen-class-refer-earn")
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def get_driver4():
    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.flipkart.com/")
    yield driver
    driver.quit()
