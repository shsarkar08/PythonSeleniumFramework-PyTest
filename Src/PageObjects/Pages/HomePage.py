from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators
from Configs.Config import TestData


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def launchUrl(self):
        self.launchurl(TestData.BASE_URL_UAT1)
        self.logger.info('Launching HPF URL')
        if self.driver.title == TestData.ACCESS_DENIED:
            self.driver.save_screenshot('./Screenshots/AccessDenied.png')
            self.logger.error('Verify if The VPN is connected')
            raise Exception
        else:
            self.driver.save_screenshot('./Screenshots/Test.png')
            self.logger.info('URL launched successfully')

    def clickSignIn(self):
        self.click(PageLocators.SignInLink)
        self.logger.info(f'Navigated to Page: {self.driver.title}')
        self.logger.info(f'URL: {self.driver.current_url}')
