import time

from Src.PageObjects.Locators import PageLocators
from Tests.Scripts.test_base import TestBase
from Src.PageObjects.Pages.LoginPage import LoginPage
from Configs.Config import TestData
from Utilities import ExcelUtils


class TestLoginDDT(TestBase):
    path = './/TestData//LoginDDT.xlsx'

    def test_excel(self):
        rows = ExcelUtils.getRowCount(self.path, 'LoginData')
        print(f'No of rows: {rows}')

        cols = ExcelUtils.getColumnCount(self.path, 'LoginData')
        print(f'No of columns: {cols}')


