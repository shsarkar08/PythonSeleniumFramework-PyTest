import time
from Tests.Scripts.test_base import TestBase
from Src.PageObjects.Pages.LoginPage import LoginPage
from Configs.Config import TestData


class TestLogin(TestBase):

    def test_clickCreateAccountLink(self):
        self.loginPage = LoginPage(self.driver)

        self.loginPage.logger.info('==== LoginPage Test Begins =====')
        self.loginPage.launchURL()
        self.loginPage.adminLogin()
        page_url = self.driver.current_url
        if page_url == TestData.DASHBOARD_URL:
            self.loginPage.logger.info('Navigated to Dashboard Successfully')
            time.sleep(2)
            self.driver.save_screenshot('./Screenshots/DashBoardPage.png')
        else:
            assert False
        self.loginPage.logger.info(f'==== End of Test for {__name__} =====')
