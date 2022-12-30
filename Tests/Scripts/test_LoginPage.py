from Tests.Scripts.test_base import TestBase
from Src.PageObjects.Pages.HomePage import HomePage
from Src.PageObjects.Pages.LoginPage import LoginPage


class TestLogin(TestBase):

    def test_clickCreateAccountLink(self):
        self.homePage = HomePage(self.driver)
        self.homePage.launchUrl()
        self.homePage.clickSignIn()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.logger.info('==== LoginPage Test Begins =====')
        self.loginPage.clickCreateNewAccount()
        self.loginPage.logger.info(f'==== End of Test for {__name__} =====')
