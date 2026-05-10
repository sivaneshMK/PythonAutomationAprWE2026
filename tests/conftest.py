import base64
import os
import time

import pytest
import pytest_html.extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    return driver

@pytest.fixture(scope ='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.foundit.in/")
    driver.maximize_window()
    driver.implicitly_wait(10)

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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            folder= "screenshots"
            os.makedirs(folder, exist_ok=True)
            file_path = os.path.join(folder, f"{item.name}_{int(time.time())}.png")
            driver.save_screenshot(file_path)

            with open(file_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode()

            # attach screenshot to the report
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.png(encoded_image))
            report.extra = extra

