from faker import Faker
from random import randint
import os


def data_usergen():

    fake = Faker()
    firstname = fake.unique.first_name()
    rand_int = randint(99, 9999)
    username = firstname+str(rand_int)
    return str(username)


class TestData:
    DEFAULT_BROWSER = 'chrome'
    ROOT_DIR = os.path.split(os.environ['VIRTUAL_ENV'])[0]
    # LOG_CONFIG_PATH = './Configs/LogConfig.yaml'
    LOG_CONFIG_PATH = f'{ROOT_DIR}/Configs/LogConfig.yaml'

    BASE_URL = 'https://opensource-demo.orangehrmlive.com/'
    DASHBOARD_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    ADMIN_USERNAME = 'Admin'
    ADMIN_PASSWORD = 'admin123'
    LOGIN_PAGE_TITLE = 'Login'
    USERNAME = data_usergen()
    PASSWORD = 'ShahTest#'
    EMAIL = USERNAME+'@mailinator.com'
