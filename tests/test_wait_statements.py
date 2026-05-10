import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import utility.common_util


def test_is_enabled():
    option = Options()
    option.add_experimental_option("detach",True)

    driver = webdriver.Chrome(option)
    driver.get("https://retail.santander.co.uk/olb/app/logon/access/#/logon")
    
    wait = WebDriverWait(driver, 10)

    cookie_banner = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='Cookie banner']//h2[text()='We use cookies to give you the best online experience']")))

    if cookie_banner.is_displayed():
        print("The cookie banner is displayed")
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler' and text()='Accept all' ]").click()
        wait.until(EC.invisibility_of_element_located((By.XPATH,
                                                     "//div[@aria-label='Cookie banner']//h2[text()='We use cookies to give you the best online experience']")))
    else:
        print("The cookie banner is not displayed")

    log_on_btn = driver.find_element(By.XPATH, "//span[text()='Log on']/parent::button")

    assert log_on_btn.is_enabled() == False, "Logon button is enabled when input fields are empty"

    remember_me_checkbox =driver.find_element(By.XPATH, "//input[@id='rememberme']")

    if remember_me_checkbox.is_selected():
        print("The remember me check box is selected")
    else:
        driver.find_element(By.XPATH,"//input[@id='rememberme']//following-sibling::span[@class='checkmark']").click()
    utility.common_util.take_screenshot(driver)


def test_alerts():
    option = Options()
    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(option)
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
    wait= WebDriverWait(driver, 10)
    alert_flag = wait.until(EC.alert_is_present())
    if alert_flag:
        print("alert is displayed")
        #driver.switch_to.alert.accept()
        alert = driver.switch_to.alert
        print(alert.text)
        alert.dismiss()
    driver.find_element(By.XPATH, "//button[@id='promtButton']").click()

    if wait.until(EC.alert_is_present()):
        print("The prompt is displayed")
    else:
        print("the prompt is not displayed")

    prompt = driver.switch_to.alert
    prompt.send_keys("pooja Raghuraman")
    prompt.accept()

@pytest.mark.wip
def test_company_windows(driver):
    driver = driver

    companies = driver.find_elements(By.XPATH, "//a[@class='flex items-center ']/img")
    print("No of companies: ",len(companies))
    companies_list = []
    for company in companies:
        title = company.get_attribute("title")
        print(title)
        companies_list.append(title)
    companies_list = set(companies_list)
    # click first 7 companies

    for company in companies_list:
        xpath = "//a[@class='flex items-center ']/img[@title='"+company+"']"
        wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
        comp = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, xpath)))
        comp.click()

    # get current window reference
    parent_window = driver.current_window_handle

    # get all the window including parent
    all_windows = driver.window_handles

    # switch to the second window
    #driver.switch_to.window(all_windows[1])

    # I have to switch to all the windows and have to get titles

    for child_window in all_windows:
        if parent_window != child_window:
            driver.switch_to.window(child_window)
            print("Switched to the child window")
        print(driver.title)
    raise Exception("dummy")