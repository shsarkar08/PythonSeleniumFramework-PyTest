from faker import Faker
from random import randint


def data_usergen():

    fake = Faker()
    firstname = fake.unique.first_name()
    rand_int = randint(99, 9999)
    username = firstname+str(rand_int)
    return str(username)


class TestData:
    DEFAULT_BROWSER = 'chrome'
    BASE_URL_UAT1 = 'https://uat.wahpf.org/us/en/home-page.html'
    BASE_URL_UAT2 = 'https://uat2.wahpf.org/us/en/home-page.html'
    LOG_CONFIG_PATH = './Configs/LogConfig.yaml'
    USERNAME = data_usergen()
    PASSWORD = 'Shah0893#'
    EMAIL = USERNAME+'@mailinator.com'
    ABOUT_YOU_PAGE_URL = 'https://uat.wahpf.org/HBEWeb/DisplayAboutYou'
    ACCESS_DENIED = 'Access denied'
