import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from src.pages.base import BasePage
from src.pages.locators import MainPageLocators



class MainPage(BasePage):

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_up_100(self):
        self.driver.execute_script("window.scrollBy(0,-100)", "")

    def scroll_up_200(self):
        self.driver.execute_script("window.scrollBy(0,-200)", "")

    def click_photo(self):
        test = self.find_clickable_element(MainPageLocators.PHOTO)
        test.click()

    def get_img(self):
        img = self.find_clickable_element(MainPageLocators.IMG)
        return img

    def next_page(self):
        test = self.find_element(MainPageLocators.NEXT_PAGE)
        return test

    def shadow_host(self):
        test = self.find_clickable_element(MainPageLocators.SHADOW_HOST)
        return test

    def shadow_content(self):
        test = self.find_clickable_element(MainPageLocators.SHADOW_CONTENT).text
        return test

    def get_widget_id(self):
        test = self.find_clickable_element(MainPageLocators.WIDGET_ID).get_attribute("widgetid")
        return test

    def click_esc(self):
        time.sleep(0.5)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def click_allow_all_eng(self):
        test = self.find_clickable_element(MainPageLocators.ALLOW_ALL)
        test.click()

    def click_allow_all_greece(self):
        test = self.find_clickable_element(MainPageLocators.ALLOW_ALL_GREECE)
        test.click()

    def click_allow_all_hebrew(self):
        test = self.find_clickable_element(MainPageLocators.ALLOW_ALL_HEBREW)
        test.click()

    def click_allow_all(self):
        test = self.find_clickable_element(MainPageLocators.ALLOW_ALL_UNIVERSAL)
        test.click()
