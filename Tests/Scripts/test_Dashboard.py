import time

from Src.PageObjects.Pages.DashboardPage import DashboardPage
from Src.PageObjects.Pages.LoginPage import LoginPage
from Tests.Scripts.test_base import TestBase
from Configs.Config import TestData
from Src.PageObjects.Locators import PageLocators


class TestDashboard(TestBase):

    def test_addNewUser(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.launchURL(TestData.BASE_URL)
        self.loginPage.adminLogin(TestData.ADMIN_USERNAME, TestData.ADMIN_PASSWORD)

        self.dashboardPage = DashboardPage(self.driver)
        self.dashboardPage.logger.info('==== DashboardPage Test Begins =====')
        ''' Navigate to Admin Module '''

        self.dashboardPage.navigateToAdminModule()
        page_url = self.driver.current_url
        if page_url == TestData.ADMIN_MODULE_URL:
            self.dashboardPage.logger.info('Navigated to Admin module successfully')
            time.sleep(2)
            self.driver.save_screenshot('./Screenshots/AdminModulePage.png')
        else:
            raise Exception

        header = self.dashboardPage.findelement(PageLocators.AdminTopbarHeader).text
        nav_header = self.dashboardPage.splitlines(header)
        assert nav_header == TestData.ADMIN_MODULE_TOPBAR_TEXT
        self.dashboardPage.logger.info(f'Header: {nav_header}')

        ''' Click on Add button from Admin Module '''
        self.dashboardPage.navigateToAddUser()
        try:
            assert self.driver.current_url == TestData.ADD_USER_PAGE_URL
            self.dashboardPage.logger.info('Navigated to Add user page successfully')
            time.sleep(2)
            self.driver.save_screenshot('./Screenshots/AddUserPage.png')
        except Exception:
            raise AssertionError

        self.dashboardPage.logger.info('Adding New User is in progress')

        ''' Tests to check if User role & status set are correct '''
        self.dashboardPage.setUserRoleAndStatus()

        user_role = self.dashboardPage.findelement(PageLocators.UserSelected).text
        self.dashboardPage.logger.info(f'User role selected as: {user_role}')
        try:
            assert user_role == TestData.USER_ROLE
        except Exception as e:
            self.dashboardPage.logger.fatal(e)
            raise AssertionError

        user_status = self.dashboardPage.findelement(PageLocators.StatusSelected).text
        self.dashboardPage.logger.info(f'User status selected as: {user_status}')
        try:
            assert user_status == TestData.USER_STATUS
        except Exception as e:
            self.dashboardPage.logger.fatal(e)
            raise AssertionError

        ''' Tests for Employee Name & Username '''
        self.dashboardPage.setEmpNameAndUsername()

        '''Set Password fields'''
        self.dashboardPage.setPassword()

        '''Add User'''
        self.dashboardPage.addUser()
        time.sleep(3)
        try:
            assert self.driver.current_url == TestData.ADMIN_MODULE_URL
            self.dashboardPage.logger.info('User has been added successfully')

            # self.driver.save_screenshot('./Screenshots/AddUserSuccess.png')
        except Exception:
            raise AssertionError

        self.dashboardPage.logger.info(f'==== End of Test for {__name__} =====')
