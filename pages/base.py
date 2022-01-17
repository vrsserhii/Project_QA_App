import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=5)

    def fill_field(self, locator, value, by=By.XPATH):
        """Fill field using provided various"""
        username = self.wait_until_element_enebled(by=by, value=locator)
        username.clear()
        username.send_keys(value)

    def wait_until_find_element(self, value, by=By.XPATH):
        """Wait until find elements"""
        return self.wait.until(EC.visibility_of_element_located(locator=(by, value)))

    def wait_until_element_enebled(self, value, by=By.XPATH):
        """Wait until element is eneble"""
        element = self.wait_until_find_element(by=by, value=value)
        return self.wait.until(EC.element_to_be_clickable(element))
