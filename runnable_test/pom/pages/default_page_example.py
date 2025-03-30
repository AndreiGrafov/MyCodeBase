from runnable_test import config
from runnable_test.pom.base import BasePage
from runnable_test.pom.locators import DefaultPageLocators

class DefaultPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser, config.Urls.TEST_WEBSITE)

    def click_form_fields(self):
        test = self.find_element_clickable(DefaultPageLocators.FORM_FIELDS)
        test.click()

    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

