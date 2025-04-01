from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import UnexpectedAlertPresentException, \
    ElementClickInterceptedException
import time
from random import randint




class BasePage:
    TIMEOUT = 2
    RANDOM_START = 1
    RANDOM_END = 2
    MSG = "Can't find element by locator ({0})"

    def __init__(self, driver, base_url=''):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, timeout=TIMEOUT):
        time.sleep(randint(BasePage.RANDOM_START, BasePage.RANDOM_END))
        return WebDriverWait(
            self.driver, timeout).until(ec.presence_of_element_located(locator),
                                        message=BasePage.MSG.format(locator))

    def find_clickable_element(self, locator, timeout=TIMEOUT):
        time.sleep(randint(BasePage.RANDOM_START, BasePage.RANDOM_END))
        return WebDriverWait(
            self.driver, timeout).until(ec.element_to_be_clickable(locator),
                                        message=BasePage.MSG.format(locator))

    def find_elements(self, locator, timeout=TIMEOUT):
        time.sleep(randint(BasePage.RANDOM_START, BasePage.RANDOM_END))
        return WebDriverWait(
            self.driver, timeout).until(ec.presence_of_all_elements_located(locator),
                                        message=BasePage.MSG.format(locator))

    def click(self, locator, timeout=TIMEOUT):
        time.sleep(randint(BasePage.RANDOM_START, BasePage.RANDOM_END))
        el = WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(locator), message=BasePage.MSG.format(locator))

        self.driver.execute_script("arguments[0].scrollIntoView();", el)

        try:
            el.click()
        except (UnexpectedAlertPresentException, ElementClickInterceptedException) as e:
            self.driver.execute_script("arguments[0].click();", el)

        return el

    def scroll(self, locator, timeout=TIMEOUT):
        time.sleep(randint(BasePage.RANDOM_START, BasePage.RANDOM_END))
        el = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator), message=BasePage.MSG.format(locator))

        self.driver.execute_script("arguments[0].scrollIntoView();", el)
        return el

    def scrolls(self, locator, timeout=TIMEOUT):
        time.sleep(randint(BasePage.RANDOM_START, BasePage.RANDOM_END))
        els = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_all_elements_located(locator),
            message=BasePage.MSG.format(locator))

        for el in els:
            self.driver.execute_script("arguments[0].scrollIntoView();", el)
            time.sleep(0.5)

    def clicks(self, locator, timeout=TIMEOUT):
        time.sleep(randint(BasePage.RANDOM_START, BasePage.RANDOM_END))
        els = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_all_elements_located(locator),
            message=BasePage.MSG.format(locator))

        for el in els:
            el.click()
            time.sleep(0.5)

    def get_driver(self):
        return self.driver

    def get_page_source(self):
        return self.driver.page_source

    def open(self, url=None):
        if url is None:
            url = self.base_url

        # logger.info(f"Go to url ({url})")

        res = self.driver.get(url)
        time.sleep(randint(BasePage.RANDOM_START, BasePage.RANDOM_END))
        return res

