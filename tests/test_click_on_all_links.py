import pytest
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_click_on_all_the_courses(get_driver3):
    driver = get_driver3
    courses = driver.find_elements(By.XPATH, "//span[text()='Know more']/parent::span/parent::div/parent::a/parent::div")
    for course in courses:
        course.click()

@pytest.mark.sanity
def test_get_all_courses(get_driver3):
    driver = get_driver3
    courses = driver.find_elements(By.XPATH, "//span[text()='Know more']/parent::span/parent::div/parent::a/parent::div/parent::div/preceding-sibling::div[1]")
    for course in courses:
        print(course.text)

@pytest.mark.regression
def test_click_on_all(get_driver3):
    driver = get_driver3
    courses = driver.find_elements(By.XPATH, "//span[text()='Know more']/parent::span/parent::div/parent::a/parent::div")
    for course in courses:
        course.click()

