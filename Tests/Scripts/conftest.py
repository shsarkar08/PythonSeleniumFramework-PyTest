from Configs.Config import TestData
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chOptions
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as ffOptions
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
import os


def pytest_addoption(parser):  # get the --browser value from command line
    parser.addoption('--browser', action='store', default=TestData.DEFAULT_BROWSER)


@pytest.fixture(scope='class')
def getbrowser(request):  # return the browser value to init_driver method
    return request.config.getoption('--browser')


@pytest.fixture(scope='class')
def init_driver(request, getbrowser):
    # driver = None
    print(f'\nBrowser from getbrowser method: {getbrowser} ')
    if getbrowser == 'chrome':
        chsvc = chromeService(ChromeDriverManager().install())
        opt = chOptions()
        opt.add_argument('--incognito')
        # opt.headless = True
        opt.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

        driver = webdriver.Chrome(service=chsvc, options=opt)
    elif getbrowser == 'firefox':
        fsvc = firefoxService(GeckoDriverManager().install())
        fopt = ffOptions()
        fopt.add_argument('-private')
        # fopt.headless = True

        driver = webdriver.Firefox(service=fsvc, options=fopt)
    else:
        raise Exception(f'{getbrowser} is not a supported browser')
        # print('Pass chrome/firefox browser ..')

    request.cls.driver = driver
    driver.maximize_window()

    yield
    driver.quit()


#   Pytest HTML Report hook for adding info on Environment Section
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'HPF'
#     # config._metadata['Module Name'] = 'Create Account'
#     config._metadata['Tester'] = 'Shahnawaz'


#   Pytest HTML Report hook for dynamic report name,path
def pytest_configure(config):
    config._metadata['Project Name'] = 'HPF'
    config._metadata['Tester'] = 'Shahnawaz'
    # config._metadata['Browser'] = config.getoption('--browser')

    # set custom options only if none are provided from command line
    if not config.option.htmlpath:
        now = datetime.now()
        # create report target dir
        if not os.path.exists('Reports'):
            os.makedirs('Reports')
        report = 'Reports/'+f"report_{now.strftime('%d-%m-%Y %H-%M-%S')}"+'.html'
        config.option.htmlpath = report
        # set it to False in case of any encoding issue
        config.option.self_contained_html = True


#   Pytest HTML Report hook for removing info from Environment section
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)


#   Pytest HTML Report hook for modifying report title
def pytest_html_report_title(report):
    report.title = "Test Automation Report"
