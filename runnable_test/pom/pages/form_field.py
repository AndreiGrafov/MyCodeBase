import time

from runnable_test.pom.base import BasePage
from runnable_test.pom.locators import FormFieldsLocators

class FormField(BasePage):

    def input_name(self, text):
        test = self.find_element_clickable(FormFieldsLocators.NAME)
        test.send_keys(text)

    def input_password(self, text):
        test = self.find_element_clickable(FormFieldsLocators.PASSWORD)
        test.send_keys(text)

    def click_drink(self):
        test = self.find_element_clickable(FormFieldsLocators.DRINK)
        test.click()

    def click_color(self):
        test = self.find_element_clickable(FormFieldsLocators.COLOR)
        time.sleep(1)
        self.browser.execute_script(f"window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.pageYOffset - 70);", test)
        time.sleep(1)
        test.click()

    def click_dropdown(self):
        test = self.find_element_clickable(FormFieldsLocators.DROPDOWN)
        test.click()

    def click_dropdown_option(self):
        test = self.find_element_clickable(FormFieldsLocators.DROPDOWN_OPTION)
        test.click()

    def input_email(self, text):
        test = self.find_element_clickable(FormFieldsLocators.EMAIL)
        test.send_keys(text)

    def input_message(self, text):
        test = self.find_element_clickable(FormFieldsLocators.MESSAGE)
        test.send_keys(text)

    def click_submit(self):
        test = self.find_element_clickable(FormFieldsLocators.SUBMIT)
        test.click()

    def get_alert_text(self):
        alert = self.browser.switch_to.alert
        text = alert.text
        alert.accept()
        return text






