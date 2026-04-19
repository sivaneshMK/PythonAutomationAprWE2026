from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_user_able_search_the_product(get_driver):
    driver = get_driver
    driver.find_element(By.ID, "small-searchterms").send_keys("Mobile")


def test_select_currency(get_driver):
    driver= get_driver
    currency_dropdown = driver.find_element(By.CSS_SELECTOR, "select[aria-label='Currency selector']")
    s1 = Select(currency_dropdown)
    #s1.select_by_index(1)
    #s1.select_by_value('https://demo.nopcommerce.com/changecurrency/1?returnUrl=%2Fsearch%3Fq%3Dmobile%26cid%3D0%26mid%3D0%26advs%3Dfalse%26isc%3Dfalse%26sid%3Dfalse%26sit%3Dfalse')
    #s1.select_by_visible_text("Euro")

    # get last option from the list box
    options = s1.options
    last_option = options[len(options)-1]
    print(last_option)
    print(last_option.text)
    print(last_option.get_attribute("value"))
