from pytest_bdd.steps import given
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


CHROME_DRIVER_BINARY = 'path to binary'


@given('Launch browser and search on google')
def ui_test():
    driver = webdriver.Chrome(rf'{CHROME_DRIVER_BINARY}')
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("first test")
    driver.close()
    pass
