import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_drag_and_drop():
    option = Options()
    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(option)
    driver.get("https://demo.guru99.com/test/drag_drop.html")
    time.sleep(5)
    five_thousand = driver.find_element(By.XPATH, "(//li[@id='fourth']/a[contains(text(),'5000')])[2]")
    #//table/tbody//td//h3[contains(text(),'DEBIT SIDE')]/following-sibling::table[@id='table4']//h3[contains(text(),'Amount')]/following-sibling::div//li
    #//table/tbody//td/h3[contains(text(),'DEBIT SIDE')]/following-sibling::table[@id='table4']//h3[contains(text(),'Amount')]/following-sibling::div//li
    #//h3[contains(text(),'DEBIT SIDE')]//following-sibling::table/descendant::h3[contains(text(),'Amount')]/following-sibling::div/descendant::li
    #//ol[@id='amt7']/li
    debit_amount = driver.find_element(By.XPATH,"//table/tbody//td//h3[contains(text(),'DEBIT SIDE')]/following-sibling::table[@id='table4']//h3[contains(text(),'Amount')]/following-sibling::div//li")
    actions = ActionChains(driver)
    actions.drag_and_drop(five_thousand, debit_amount).perform()

    credit_amount = driver.find_element(By.XPATH, "//h3[contains(text(),'CREDIT SIDE')]//following-sibling::table/descendant::h3[contains(text(),'Amount')]/following-sibling::div/descendant::li")

    actions.click_and_hold(five_thousand).perform()
    actions.move_to_element(credit_amount).perform()
    actions.release().perform()

    driver.get("https://www.facebook.com/")
    time.sleep(5)
    email_txt_bx = driver.find_element(By.XPATH, "//input[@name='email']")
    email_txt_bx.send_keys("Sivanesh")
    email_txt_bx.clear()
    time.sleep(5)
    actions.click(email_txt_bx).perform()
    actions.send_keys("sivanesh").perform()
    actions.context_click(email_txt_bx).perform()
