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
    PWD_RESET_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode'
    ADMIN_MODULE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
    ADD_USER_PAGE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser'

    ADMIN_USERNAME = 'Admin'
    ADMIN_PASSWORD = 'admin123'
    LOGIN_PAGE_TITLE = 'Login'
    RESET_PWD_SUCCESS = 'Reset Password link sent successfully'

    ADMIN_MODULE_TOPBAR_TEXT = 'AdminUser Management'
    ADMIN_EMPLOYEE_NAME = 'Paul Collings'
    EMPLOYEE_TEXT = 'pa'
    USER_ROLE = 'Admin'
    USER_STATUS = 'Enabled'

    USERNAME = data_usergen()
    PASSWORD = 'ShahTest#8'
    EMAIL = USERNAME+'@mailinator.com'
