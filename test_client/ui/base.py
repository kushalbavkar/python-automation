from typing import Tuple

from selenium.webdriver.support.ui import WebDriverWait

from test_client.entities.sites import Sites
from test_client.ui import By, conditions, WebDriver, WebElement


class Base:
    def __init__(self, driver: WebDriver, timeout: int = 5):
        self.driver = driver
        self.timeout = timeout

    def navigate(self, site: Sites):
        self.driver.get(site.value)

    def find_element(self, locator: Tuple[By, str]) -> WebElement:
        return self._find(locator)

    def send_keys(self, text: str, locator: Tuple[By, str]):
        self._find(locator).send_keys(text)

    def click(self, locator: Tuple[By, str]):
        self._find(locator).click()

    def _find(self, locator: Tuple[By, str]) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(conditions.visibility_of_element_located(locator))

    def wait(self, locator: Tuple[By, str], timeout: int):
        return WebDriverWait(self.driver, timeout).until(conditions.visibility_of_element_located(locator))

