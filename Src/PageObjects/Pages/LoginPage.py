import time

from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def clickCreateNewAccount(self):
        self.click(PageLocators.CrateAccountLink)
        self.logger.info(f'Navigated to page: {self.driver.title}')
        self.logger.info(f'URL: {self.driver.current_url}')
        time.sleep(2)
