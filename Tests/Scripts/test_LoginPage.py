import time

from Src.PageObjects.Locators import PageLocators
from Tests.Scripts.test_base import TestBase
from Src.PageObjects.Pages.LoginPage import LoginPage
from Configs.Config import TestData


class TestLogin(TestBase):

    def test_adminLogin(self):
        self.loginPage = LoginPage(self.driver)

        self.loginPage.logger.info('==== LoginPage Test Begins =====')

        self.loginPage.launchURL(TestData.BASE_URL)
        login_page_title = self.loginPage.findelement(PageLocators.LoginTitle).text
        if login_page_title == TestData.LOGIN_PAGE_TITLE:
            self.driver.save_screenshot('./Screenshots/LoginPage.png')
            self.loginPage.logger.info('OrangeHRM url launched successfully')
        else:
            self.loginPage.logger.error('Unable to launch OrangeHRM url')
            self.driver.save_screenshot('./Screenshots/UrlLaunchErr.png')
            raise Exception

        self.loginPage.adminLogin(TestData.ADMIN_USERNAME, TestData.ADMIN_PASSWORD)
        page_url = self.driver.current_url
        if page_url == TestData.DASHBOARD_URL:
            self.loginPage.logger.info('Navigated to Dashboard Successfully')
            time.sleep(2)
            self.driver.save_screenshot('./Screenshots/DashBoardPage.png')
        else:
            raise Exception

        self.loginPage.logout(TestData.LOGOUT_MENU)
        time.sleep(2)

        self.loginPage.logger.info(f'==== End of Test for {__name__} =====')
