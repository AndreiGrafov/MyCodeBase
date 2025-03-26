import time

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

from automation_testing import config
from automation_testing.pom.base import BasePage
from automation_testing.pom.locators import ExamplesOfLocators

# this class contains most used methods and useful tools
class DefaultPage(BasePage):

    # this method initiates site that we are testing
    def __init__(self, browser):
        super().__init__(browser, config.Urls.PROJECT_STAGE)

    # try catch construction used to avoid test crash in situations where crash is inevitable
    def get_switch_to_property(self):
        try:
            test = self.find_element_wait(ExamplesOfLocators.EXAMPLE_WITH_TAG).is_displayed()
        except:
            test = False
        return test

    # refresh can be stored here as well
    def resfresh(self):
        self.browser.refresh()

    # this method scrolls page to the bottom
    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # pretty often click esc is way more effective than any other action))
    def click_esc(self):
        time.sleep(0.5)
        ActionChains(self.browser).send_keys(Keys.ESCAPE).perform()

    # in cases where in the middle of the test you have to open tab with another source, use this
    def open_new_tab_example(self):
        self.browser.execute_script(f"window.open('https://test-site.com/','secondtab');")
        chld = self.browser.window_handles[1]
        self.browser.switch_to.window(chld)

    # some of tests open new tab after action, here method to switch to another tab after that
    def switch_to_second_window(self):
        chld = self.browser.window_handles[1]
        self.browser.switch_to.window(chld)

    # and of course the method to return on first tab
    def switch_to_first_window(self):
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)

    # don't forget to close tab if don't need it anymore
    def close_tab(self):
        self.browser.close()

    # another strange decision, I don't remember why I wrote that, but don't repeat
    def close_tabs(self):
        for x in range(1, 10):
            try:
                self.browser.close()
                print('CLOSING TABS..........')
            except:
                print('ALL TABS ARE CLOSED...')
                break

