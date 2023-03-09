import time

from Src.BasePage.BasePage import BasePage
from Src.PageObjects.Locators import PageLocators
from Configs.Config import TestData


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigateToAdminModule(self):
        self.click(PageLocators.AdminModule)
        self.logger.info(f'Navigated to URL: {self.driver.current_url}')
        # time.sleep(2)

    def navigateToAddUser(self):
        self.click(PageLocators.AddBtn)
        self.logger.info(f'Navigated to URL: {self.driver.current_url}')
        # time.sleep(2)

    def setUserRoleAndStatus(self):
        self.click(PageLocators.UserRoleDropDownArrow)
        self.click(PageLocators.UserRoleAdmin)
        self.click(PageLocators.StatusDropDownArrow)
        self.click(PageLocators.Status)

    def setEmpNameAndUsername(self):
        username = TestData.USERNAME
        self.set_text_value(PageLocators.EmpUsername, username)
        self.logger.info(f'Username set as: {username}')

        self.set_text_value(PageLocators.EmployeeName, TestData.EMPLOYEE_TEXT)
        time.sleep(2)
        emps = self.findelements(PageLocators.EmployeeNameSuggestions)
        self.logger.info(f'Emp name suggestion count: {len(emps)}')
        for emp in emps:
            flag = False
            print(emp.text)
            if emp.text == TestData.ADMIN_EMPLOYEE_NAME:
                flag = True
                emp.click()
                break

        if not flag:
            self.logger.error('Employee Not found in Suggestions list')
            assert False

    def setPassword(self):
        self.set_text_value(PageLocators.Password, TestData.PASSWORD)
        self.set_text_value(PageLocators.ConfirmPassword, TestData.PASSWORD)

    def addUser(self):
        self.click(PageLocators.SaveBtn)
        time.sleep(3)
        self.driver.save_screenshot('./Screenshots/AddUserSuccess.png')
