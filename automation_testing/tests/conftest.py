import time

import pytest
from selenium import webdriver

from automation_testing import config
from automation_testing.pom.pages import LoginPage
from automation_testing.pom.pages import DefaultPage
from selenium.webdriver.chrome.service import Service

# this is one of the most important module in framework
# it completes two missions:
# 1 - sets up perameters of test run
# 2 - here we write what happens before test and what happens after test

# path to our druver and parameter headless or non-headless run
def pytest_addoption(parser):
    parser.addoption("--driver_path", action="store", default="D:\pythonSDKs\Python310\chromedriver.exe")
    parser.addoption("--headless", action="store", default="0")

@pytest.fixture(scope='session')
def driver_path(pytestconfig):
    return pytestconfig.getoption("driver_path")

@pytest.fixture(scope='session')
def headless(pytestconfig):
    return pytestconfig.getoption("headless")


# global fixture for parameters of run, it also closes browser after run
@pytest.fixture(scope="session")
def browser(driver_path, headless):
    print("\nstart browser for test..")

    options = webdriver.ChromeOptions()
    if headless == '1':
        options.add_argument("--headless")

    # this window-size shit fails quit command and overloads pc with trash
    # options.add_argument("window-size=1920,1080")
    # options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(executable_path=driver_path)
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    time.sleep(1)

    yield browser
    print("\nquit browser..")
    time.sleep(0.5)
    browser.quit()

# internal fixture for authorization
# parameter of fixture is browser fixture
@pytest.fixture(scope="module")
def login_as_admin_example(browser):
    login = LoginPage(browser)
    login.open()
    default = DefaultPage(browser)
    time.sleep(0.8)
    # go to login
    time.sleep(0.5)
    login.login(config.Credentials.ADMIN)
    time.sleep(0.5)
    yield browser
    # logout
    time.sleep(0.5)
