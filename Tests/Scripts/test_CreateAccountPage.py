from Tests.Scripts.test_base import TestBase
from Src.PageObjects.Pages.HomePage import HomePage
from Src.PageObjects.Pages.LoginPage import LoginPage
from Src.PageObjects.Pages.CreateAccountPage import CreateAccount


class TestCreateAccount(TestBase):

    def test_createAccount(self):
        self.homePage = HomePage(self.driver)
        self.homePage.launchUrl()
        self.homePage.clickSignIn()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.clickCreateNewAccount()

        self.createaccount = CreateAccount(self.driver)
        self.createaccount.logger.info('==== CreateAccountPage Test Begins =====')
        self.createaccount.createNewAccount()
        self.createaccount.urlVerify()
        self.createaccount.logger.info(f'==== End of Test for {__name__} =====')
