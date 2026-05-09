import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_alert_popup():
    option = Options()
    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(option)
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
    time.sleep(3)

    #driver.switch_to.alert.accept()
    alert = driver.switch_to.alert
    print(alert.text)

    alert.dismiss()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
    time.sleep(3)
    prompt = driver.switch_to.alert
    prompt.send_keys("pooja Raghuraman")
    prompt.accept()