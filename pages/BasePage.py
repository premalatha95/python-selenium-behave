from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from typing import Tuple

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator: Tuple[str, str]):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill_text(self, locator: Tuple[str, str], string: str):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(string)

    def switch_to_active_tab(self):
        current_window = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        else:
            self.driver.close()

