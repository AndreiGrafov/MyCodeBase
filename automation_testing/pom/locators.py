from selenium.webdriver.common.by import By

class ExamplesOfLocators:
    # most often example of locators by xpath
    EXAMPLE_WITH_TEXT = (By.XPATH, '//button[contains(text(), "Log out")]')
    EXAMPLE_WITH_EXACT_MATCH = (By.XPATH, '//a[text() = "Offers"]')
    EXAMPLE_WITH_TAG = (By.XPATH, '//input[@name= "email"]')
    # sometimes to reach element we have to go up and down in elements tree ierarchy, in that case ancestor used
    ANCESTOR_EXAMPLE = (By.XPATH, '//a[contains(text(), "Terms and conditions")]/ancestor::label/span')
    # even if method "By.ID" exists it is easier to find element like this
    ID_TAG_EXAMPLE = (By.XPATH, '//input[@id= "button"]')

class LoginPageLocators:
    # although xpath is very convenient we can also use css selectors
    # these selectors locate elements by ID, # - symbol for ID's
    LOGIN = (By.CSS_SELECTOR, '#login')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    ENTER = (By.XPATH, "//div/button[text() = 'enter']")
    LOGIN_ERROR = (By.XPATH, "//div/button[text() = 'invalid credentials']")
    FIELD_IS_REQUIRED = (By.XPATH, "//div/button[text() = 'password is required']")