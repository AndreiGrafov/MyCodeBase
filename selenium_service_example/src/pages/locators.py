from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "#username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN = (By.XPATH, "//button[text()='Sign in']")


class CompanyPageLocators:
    EMPLOYEES = (By.XPATH, '//a[contains(@href, "/search/results/people/?currentCompany")]')


class PaginationPageLocators:
    ITEMS = (By.CSS_SELECTOR, 'li.reusable-search__result-container  a > span')
    NEXT = (By.XPATH, '//button[@aria-label="Next"]')
    LAST_ITEM = (By.CSS_SELECTOR, "div.search-results-container ul:nth-child(1) > li:last-child")

class MainPageLocators:
    CARS = (By.XPATH, "//div[@class = 'row']/div/div/div[2]/h4")
    PHOTO = (By.XPATH, "//div[@class = 'row']/div[2]/div/div/div")
    IMG = (By.XPATH, '//img')
    NEXT_PAGE = (By.XPATH, '//li/a[contains(text(), "»")]')

    SHADOW_HOST = (By.XPATH, '//book-a-space-widget')
    SHADOW_CONTENT = (By.XPATH, '//h3')
    WIDGET_ID = (By.XPATH, "//book-a-space-widget")
    ALLOW_ALL = (By.XPATH, "//a[text() ='Allow all']")
    ALLOW_ALL_GREECE = (By.XPATH, "//a[text() ='Να επιτρέπονται όλα']")
    ALLOW_ALL_HEBREW = (By.XPATH, "//a[text() ='לאשר הכול']")
    ALLOW_ALL_UNIVERSAL = (By.XPATH, '//a[@id = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')

class NISPageLocators:
    NIS = (By.XPATH, "//font[contains(text(), 'NIS')]")


class UserPageLocators:
    FOLLOW = (By.XPATH, '//span[contains(text(), "Write a review")]')
    RESPONSE_TIME = (By.XPATH, '//div[@id = "raq-widget"]/div/div/div/div/p[2]')
    RESPONSE_RATE = (By.XPATH, '//div[@id = "raq-widget"]/div/div/div/div[2]/div/p[2]')
    ALL_CPA = (By.XPATH, '//h3/span/a')