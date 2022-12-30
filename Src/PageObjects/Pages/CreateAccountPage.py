from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators
from Configs.Config import TestData
import time


class CreateAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def createNewAccount(self):
        self.set_text_value(PageLocators.Username, TestData.USERNAME)
        self.set_text_value(PageLocators.Password, TestData.PASSWORD)
        self.set_text_value(PageLocators.PasswordVerify, TestData.PASSWORD)
        self.set_text_value(PageLocators.Email, TestData.EMAIL)
        self.set_text_value(PageLocators.EmailVerify, TestData.EMAIL)
        self.click(PageLocators.NotificationPref)
        self.click(PageLocators.TermsAndConditions)
        self.click(PageLocators.CreateAccountBtn)
        time.sleep(2)

    def urlVerify(self):
        current_url = self.driver.current_url
        self.logger.info(f'Navigated to Page: {self.driver.title}')
        assert current_url == TestData.ABOUT_YOU_PAGE_URL
