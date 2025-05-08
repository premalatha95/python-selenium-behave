from pages.BasePage import BasePage


class Launcher(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.get("https://www.automationexercise.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)