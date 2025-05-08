from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage


class LoginPage(BasePage):

    name_field = (By.NAME, 'name')
    email_field = (By.NAME, 'email')
    submit_button = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sign_up_with(self, name, email):
        self.fill_text(self.name_field, name)
        self.fill_text(self.email_field, email)
        self.click(self.submit_button)
        pass