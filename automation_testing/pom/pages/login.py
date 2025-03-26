import time

from automation_testing import config
from automation_testing.pom.base import BasePage
from automation_testing.pom.locators import LoginPageLocators


class LoginPage(BasePage):
    # inherited method from base, place out project url here
    def __init__(self, browser):
        super().__init__(browser, config.Urls.PROJECT_STAGE)

    # here methods to provide login process
    def enter_username(self, username):
        username_el = self.find_element_clickable(LoginPageLocators.LOGIN)
        username_el.send_keys(username)

    def enter_password(self, password):
        password_el = self.find_element_clickable(LoginPageLocators.PASSWORD)
        password_el.send_keys(password)

    def click_enter(self):
        enter = self.find_element_clickable(LoginPageLocators.ENTER)
        enter.click()

    # and then enter login and password using parametrized method
    def login(self, credentials):
        time.sleep(0.3)
        self.enter_username(credentials[0])
        time.sleep(0.3)
        self.enter_password(credentials[1])
        self.click_enter()

    # examples of negative checks for login
    def get_login_error(self):
        test = self.find_element_wait(LoginPageLocators.LOGIN_ERROR).text
        return test

    def get_field_is_required_1(self):
        test = self.find_many_elements_wait(LoginPageLocators.FIELD_IS_REQUIRED)
        return test[0].text

