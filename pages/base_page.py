from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions

class BasePage:
    _url = None

    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get(self._url)

    def get_element(self, selector_type, selector, timeout=10):
        return WebDriverWait(self._driver, timeout=timeout).until(
            expected_conditions.visibility_of_element_located((getattr(By, selector_type), selector)))

    def get_elements(self, selector_type, selector, timeout=10):
        return WebDriverWait(self._driver, timeout=timeout).until(
            expected_conditions.visibility_of_any_elements_located((getattr(By, selector_type), selector)))

    def text_is_displayed(self, text, timeout=10):
        expression = "//*[contains(text(), '" + text + "')]"
        return WebDriverWait(self._driver, timeout=timeout).until(
            expected_conditions.visibility_of_any_elements_located((By.XPATH, expression)))