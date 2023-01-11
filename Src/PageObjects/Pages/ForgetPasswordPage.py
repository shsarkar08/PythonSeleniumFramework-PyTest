from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators
from Configs.Config import TestData
import time


class ForgetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigatePwdResetPage(self):
        self.click(PageLocators.ForgotPwd)
        self.logger.info('Navigating to Reset Password Page')
        time.sleep(2)

    def resetPassword(self):
        self.set_text_value(PageLocators.Username, TestData.USERNAME)
        self.click(PageLocators.ResetBtn)
