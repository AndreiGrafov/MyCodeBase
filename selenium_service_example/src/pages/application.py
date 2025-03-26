from selenium.webdriver.chrome.service import Service

from src.pages.base import BasePage
from src.pages.main_page import MainPage
from selenium import webdriver

import os



class Application:
    HEADLESS = 1
    DRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")

    def __init__(self):

        service = Service(executable_path=Application.DRIVER_PATH)
        options = webdriver.ChromeOptions()

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')

        if Application.HEADLESS == 1:
            options.add_argument("--headless")
            options.add_argument("window-size=1920,1080")

        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

        self.base = BasePage(self.driver)
        self.main = MainPage(self.driver)

    def go_to(self, url):
        self.base.open(url)

    def get_page_source(self):
        page_source = self.driver.page_source
        return page_source

    def close(self):
        self.driver.quit()

