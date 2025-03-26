import time

import pyautogui
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

from automation_testing.pom.base import BasePage
from automation_testing.pom.locators import ExamplesOfLocators

#this class inherits all the methods from Base
class ExamplePage(BasePage):

    #this method click on element
    def click_example(self):
        test = self.find_element_clickable(ExamplesOfLocators.EXAMPLE_WITH_TEXT)
        test.click()

    #this method inputs something you enter into method parameter to given element
    def input_example(self, text):
        test = self.find_element_clickable(ExamplesOfLocators.EXAMPLE_WITH_TAG)
        test.send_keys(text)

    #this method is basic from documentation, but it's not reliable, so I usually use other
    def clear_example_1(self):
        test = self.find_element_clickable(ExamplesOfLocators.EXAMPLE_WITH_EXACT_MATCH)
        test.clear()

    #this one is better but takes time
    def clear_example_2(self):
        test = self.find_element_clickable(ExamplesOfLocators.EXAMPLE_WITH_EXACT_MATCH)
        for x in range(100):
            test.send_keys(Keys.BACKSPACE)

    # this one is the best for now
    def clear_example_3(self):
        test = self.find_element_clickable(ExamplesOfLocators.EXAMPLE_WITH_EXACT_MATCH)
        test.send_keys(Keys.BACKSPACE * 100)

    # when you need to pick one exact element you can use this, be careful you have to set iterator manually
    def click_one_of_many_example(self, i):
        test = self.find_many_elements_wait(ExamplesOfLocators.EXAMPLE_WITH_EXACT_MATCH)
        test[i].click()

    # this method returns number of found components, that can be further used as parameter for cycle
    def get_number_of_example(self):
        test = self.find_many_elements_wait(ExamplesOfLocators.EXAMPLE_WITH_EXACT_MATCH)
        num_of_widgets = len(test)
        return num_of_widgets

    # sometimes system needs additional actions to perform, like keyboard manipulation
    def input_widget_id(self, text):
        test = self.find_element_clickable(ExamplesOfLocators.EXAMPLE_WITH_EXACT_MATCH)
        test.send_keys(text)
        test.send_keys(Keys.ENTER)

    # of course good tests ot only send information, they also receive it, this is basic getter to take text
    # from element of page
    def get_text_example(self):
        test = self.find_element_wait(ExamplesOfLocators.EXAMPLE_WITH_EXACT_MATCH).text
        return test

    # sometimes situation requires unusual approach, for example to inject variable into xpath
    # this ruins concept of isolated locators, but this solution atleast works properly
    # method takes number from parameters and inserts it to locator, then clicks on calendar date
    def example_click_certain_day(self, day):
        time.sleep(1)
        day = str(day)
        CERTAIN_DAY = (By.XPATH, f'//div[@role= "grid"]/div/div/div/button[text() = "{day}"]')
        test = self.find_element_clickable(CERTAIN_DAY)
        test.click()

    # some of test cases have process of uploading on one of the steps, it's a bit complicated task
    # here one of solutions, picture stored in project folder
    def upload_logo_photo(self):
        test = self.find_element_clickable(ExamplesOfLocators.EXAMPLE_WITH_EXACT_MATCH)
        test.click()
        time.sleep(2)
        pyautogui.write(r'D:\project_photos\photo1.png')
        pyautogui.press('enter')
        time.sleep(1)



