from selenium.webdriver.common.by import By

class DefaultPageLocators:
    FORM_FIELDS = (By.XPATH, '//a[text() = "Form Fields"]')

class FormFieldsLocators:
    NAME = (By.XPATH, '//input[@name = "name-input"]')
    PASSWORD = (By.XPATH, '//input[@type = "password"]')
    DRINK = (By.XPATH, '//label[text()= "Wine"]')
    COLOR = (By.XPATH, '//label[text()= "Green"]')
    DROPDOWN = (By.XPATH, '//select[@id= "automation"]')
    DROPDOWN_OPTION = (By.XPATH, '//option[@value= "undecided"]')
    EMAIL = (By.XPATH, '//input[@title= "No fake emails!"]')
    MESSAGE = (By.XPATH, '//textarea[@name= "message"]')
    SUBMIT = (By.XPATH, '//button[@id= "submit-btn"]')

