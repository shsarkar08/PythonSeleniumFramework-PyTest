import time
from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators
from Configs.Config import TestData


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def launchURL(self, url):
        self.launchurl(url)
        self.logger.info('Launching OrangeHRM URL')
        time.sleep(2)

    def adminLogin(self, username, password):
        self.set_text_value(PageLocators.AdmUsername, username)
        self.set_text_value(PageLocators.AdmPassword, password)
        self.click(PageLocators.LoginBtn)
        self.logger.info(f'Navigated to URL: {self.driver.current_url}')
