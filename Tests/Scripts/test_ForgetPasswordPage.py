from Src.PageObjects.Locators import PageLocators
from Src.PageObjects.Pages.ForgetPasswordPage import ForgetPasswordPage
from Src.PageObjects.Pages.LoginPage import LoginPage
from Tests.Scripts.test_base import TestBase
from Configs.Config import TestData
import time


class TestForgetPassword(TestBase):

    def test_resetPassword(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.launchURL()

        self.forgetpasspage = ForgetPasswordPage(self.driver)
        self.forgetpasspage.logger.info('==== ForgetPasswordPage Test Begins =====')

        self.forgetpasspage.navigatePwdResetPage()
        page_url = self.driver.current_url
        if page_url == TestData.PWD_RESET_URL:
            self.forgetpasspage.logger.info('Navigated to Password Reset Page Successfully')
            time.sleep(1)
            self.driver.save_screenshot('./Screenshots/PasswordResetPage.png')
        else:
            raise Exception

        self.forgetpasspage.resetPassword()
        self.forgetpasspage.logger.info(f'Navigated to URL: {self.driver.current_url}')
        time.sleep(1)
        success_text = self.forgetpasspage.findelement(PageLocators.resetPwdSuccessText).text
        if success_text == TestData.RESET_PWD_SUCCESS:
            self.forgetpasspage.logger.info('Password Reset link has been sent')
            time.sleep(2)
            self.driver.save_screenshot('./Screenshots/PasswordResetSuccess.png')

        else:
            raise Exception

        self.forgetpasspage.logger.info(f'==== End of Test for {__name__} =====')
