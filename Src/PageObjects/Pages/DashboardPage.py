import time

from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators
from Configs.Config import TestData


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigateToAdminModule(self):
        self.click(PageLocators.AdminModule)
        self.logger.info(f'Navigated to URL: {self.driver.current_url}')
        time.sleep(2)

    def navigateToAddUser(self):
        self.click(PageLocators.AddBtn)
        self.logger.info(f'Navigated to URL: {self.driver.current_url}')
        time.sleep(2)

    def addNewUser(self):
        pass
