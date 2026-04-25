import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_frame_handling(get_driver2):
    driver = get_driver2
    iframe =driver.find_element(By.XPATH,
    "//h1[text()='Drag and Drop Demo']/following-sibling::div//iframe")
    #switch to the iframe by using webelement
    #driver.switch_to.frame(iframe)
    driver.switch_to.frame(0)
    #driver.switch_to.frame(name attribute value or id attribute value)
    print(driver.find_element(By.XPATH, "//div[@id='playground']/p").text)
    # switch back to the default html
    # driver.switch_to.default_content()
    # text = driver.find_element(By.XPATH, "//h2[text()='Drag Details']/following-sibling::p[1]").text
    # print(text)

    goat2 = driver.find_element(By.XPATH, "//img[@class='draggable stayinparent' and @id='goat2']")
    goat0 = driver.find_element(By.XPATH, "//div[@id='playground']/img[@id='goat0']")

    actions  = ActionChains(driver)
    actions.drag_and_drop(goat2, goat0).perform()



    # perform drag and drop operation without using drag and drop method
    goat1 = driver.find_element(By.XPATH, "//div[@id='playground']/img[@id='goat1']")
    goat3 = driver.find_element(By.XPATH, "//div[@id='playground']/img[@id='goat3']")

    actions.click_and_hold(goat1).perform()
    actions.move_to_element(goat3).perform()

    actions.release().perform()
    time.sleep(5)