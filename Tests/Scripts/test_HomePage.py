from Src.PageObjects.Pages.HomePage import HomePage
from Tests.Scripts.test_base import TestBase


class TestHome(TestBase):

    def test_clickSignIn(self):
        self.homepage = HomePage(self.driver)
        self.homepage.logger.info('==== Homepage Test Begins =====')
        self.homepage.launchUrl()
        self.homepage.clickSignIn()
        self.homepage.logger.info(f'==== End of Test for {__name__} =====')
