import time

from selenium.webdriver.common.by import By


def test_company_windows(get_driver1):
    driver = get_driver1
    time.sleep(10)
    companies = driver.find_elements(By.XPATH, "//a[@class='flex items-center ']/img")
    print(len(companies))
    companies_list = []
    for company in companies:
        title = company.get_attribute("title")
        print(title)
        companies_list.append(title)
    companies_list = set(companies_list)
    # click first 7 companies

    for company in companies_list:
        xpath = "//a[@class='flex items-center ']/img[@title='"+company+"']"
        driver.find_element(By.XPATH, xpath).click()

    time.sleep(30)

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


