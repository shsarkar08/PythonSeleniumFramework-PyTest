from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from Utilities.Logger_new import Pylog


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = Pylog.logr('test')

    def launchurl(self, url):
        try:
            return self.driver.get(url)
        except Exception as e:
            self.logger.error(f'Unable to Launch URL: {e}', exc_info=True)

    def findelement(self, locator_properties):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                cond.visibility_of_element_located(locator_properties))
            return elem
            # return self.driver.find_element(*locator_properties)

        except TimeoutException:
            # except NoSuchElementException:
            self.logger.error('Having trouble finding the element', exc_info=True)

    def findelements(self, locator_properties):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                cond.visibility_of_all_elements_located(locator_properties))
            return elem
            # return self.driver.find_elements(*locator_properties)

        except TimeoutException:
            # except NoSuchElementException:
            self.logger.error('Having trouble finding the element', exc_info=True)

    def click(self, by_locator):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                cond.visibility_of_element_located(by_locator))
            elem.click()
        except TimeoutException:
            self.logger.error('Unable to click', exc_info=True)

    def set_text_value(self, locator_properties, set_text):

        try:
            self.findelement(locator_properties).send_keys(set_text)
            self.logger.info(f'Entered Value: {set_text}')
            return set_text

        except Exception as e:
            self.logger.error(f'Unable to set text: {e}', exc_info=True)

    def splitlines(self, value):
        return ''.join(value.splitlines())
