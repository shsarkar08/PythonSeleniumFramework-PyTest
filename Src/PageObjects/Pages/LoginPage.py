import time
from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators


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

    def logout(self, logoutmenu):
        self.click(PageLocators.UserDropDownCaret)
        options = self.findelements(PageLocators.DropDownMenus)
        self.logger.info(f'Number of dropdown menus: {len(options)}')
        time.sleep(2)
        flag = False
        for opt in options:
            self.logger.info(opt.text)
            if opt.text == logoutmenu:
                flag = True
                self.logger.info(f'Option to be clicked: {opt.text}')
                opt.click()
                break
        if flag:
            self.logger.info('Logged out successfully')
        else:
            self.logger.error('Logout option not found')
