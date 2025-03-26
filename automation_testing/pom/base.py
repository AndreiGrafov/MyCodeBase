from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#every automation qa python project that uses Page Object Model has Base class

class BasePage:

    # initialization of self.browser
    def __init__(self, browser, base_url=''):
        self.browser = browser
        self.url = base_url

    #triggers browser to open
    def open(self):
        return self.browser.get(self.url)

    #custom way to open another different url that hardcoded
    def open_prod(self):
        return self.browser.get('https://www.qa-project.com/')

    #not usually used because "find_element_clickable" exists, this method only finds element but doesnt prove that
    #element can be clicked, can be used if you need to find text on page
    def find_element_wait(self, locator):
        element = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(locator))
        return element

    #the most useful method to interact with clickable components of the page
    def find_element_clickable(self, locator):
        el = WebDriverWait(self.browser, 3).until(
            EC.element_to_be_clickable(locator))
        return el

    #when there is pack of the same elements, use this one and than work with them in cycle or pick one, obviously you
    #can't click on list of elements, so it's not "clickable" type
    def find_many_elements_wait(self, locator):
        elements = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located(locator))
        return elements

    #my own invention used only once when I had to check if element has property to be clicked(actually pretty useless)
    def find_element_is_clickable(self, locator):
        try:
            el = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(locator))
            return el.click()
        except:
            print("ELEMENT IS NOT CLICKABLE")

    # refreshes page can be call from there of from any other class, for example from default (better from here)
    def resfresh(self):
        self.browser.refresh()
