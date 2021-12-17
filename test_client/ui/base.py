from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait

from test_client.entities.sites import Sites
from test_client.ui.webdriver import WebDriver


class Base:
    def __init__(self, driver: WebDriver, timeout: int = 5):
        self.driver = driver
        self.timeout = timeout

    def navigate(self, site: Sites):
        self.driver.get(site.value)

    def find_element(self, locator: Tuple[By, str]):
        self._find(locator)

    def _find(self, locator: Tuple[By, str]):
        return WebDriverWait(self.driver, self.timeout).until(conditions.visibility_of_element_located(locator))
