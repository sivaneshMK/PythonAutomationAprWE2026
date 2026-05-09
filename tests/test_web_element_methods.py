import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_filter_functions(get_driver4):
    driver = get_driver4
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[@role='button' and text()='✕']").click()
    search_box = driver.find_element(By.XPATH, "//input[@name='q']")
    search_box.send_keys("shoes")
    time.sleep(3)
    #search_box.clear()
    for _ in range(5):
        search_box.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    search_box.send_keys("mobile")
    time.sleep(5)
    search_box.send_keys(Keys.ENTER)
    #driver.find_element(By.XPATH, "//span[text()='mobile']").click()
    time.sleep(10)
    brand_filter = driver.find_element(By.XPATH, "//div[text()='vivo']//preceding-sibling::input[@type='checkbox']")
    if brand_filter.is_selected():
        print("the vivo brand checkbox is already selected")
    else:
        driver.find_element(By.XPATH, "//div[text()='vivo']//preceding-sibling::div").click()
    time.sleep(10)

    flag = driver.find_element(By.XPATH, "//a[text()='Login']").is_displayed()
    print(flag)

def test_get_attribbute(get_driver1):
    driver = get_driver1
    time.sleep(10)
    companies = driver.find_elements(By.XPATH, "//a[@target='_blank']/img")

    for company in companies:
        print(company.get_attribute("title"))


def test_navigation_methods():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.find_element(By.XPATH, "//span[text()='Forgotten password?']").click()
    print(driver.title)
    driver.back()
    time.sleep(2)
    print(driver.title)
    driver.forward()
    print(driver.title)

def test_is_enabled():
    option = Options()
    option.add_experimental_option("detach",True)

    driver = webdriver.Chrome(option)
    driver.get("https://retail.santander.co.uk/olb/app/logon/access/#/logon")
    time.sleep(5)

    cookie_banner = driver.find_element(By.XPATH, "//div[@aria-label='Cookie banner']//h2[text()='We use cookies to give you the best online experience']")
    if cookie_banner.is_displayed():
        print("The cookie banner is displayed")
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler' and text()='Accept all' ]").click()
    else:
        print("The cookie banner is not displayed")
    time.sleep(5)
    log_on_btn = driver.find_element(By.XPATH, "//span[text()='Log on']/parent::button")

    assert log_on_btn.is_enabled() == False, "Logon button is enabled when input fields are empty"

    remember_me_checkbox =driver.find_element(By.XPATH, "//input[@id='rememberme']")

    if remember_me_checkbox.is_selected():
        print("The remember me check box is selected")
    else:
        driver.find_element(By.XPATH,"//input[@id='rememberme']//following-sibling::span[@class='checkmark']").click()