import time
from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators
from Configs.Config import TestData


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def launchURL(self):
        self.launchurl(TestData.BASE_URL)
        self.logger.info('Launching OrangeHRM URL')
        time.sleep(2)
        login_page_title = self.findelement(PageLocators.LoginTitle).text
        if login_page_title == TestData.LOGIN_PAGE_TITLE:
            self.driver.save_screenshot('./Screenshots/LoginPage.png')
            self.logger.info('OrangeHRM url launched successfully')
        else:
            self.logger.info('Unable to launch OrangeHRM url')
            self.driver.save_screenshot('./Screenshots/UrlLaunchErr.png')
            raise Exception

    def adminLogin(self):
        self.set_text_value(PageLocators.AdmUsername, TestData.ADMIN_USERNAME)
        self.set_text_value(PageLocators.AdmPassword, TestData.ADMIN_PASSWORD)
        self.click(PageLocators.LoginBtn)
        self.logger.info(f'Navigated to URL: {self.driver.current_url}')
