import time

from selenium.webdriver.common.by import By
from selenium_service_example.src.pages.application import Application

# this is class where all functionality is realised, and all errors are caught
class Scraper:

    def __init__(self):
        self.app = Application()

    # closes browser
    def close(self):
        self.app.close()
        # logger.info("Browser is closed")

    # huge method that checks test object
    def scrape_main_screen(self, widget):
        time.sleep(0.1)
        #action here
        try:
            # for debug in headless mode we can take screenshots
            # self.app.driver.save_screenshot('screenshot.png')
            try:
                # here test hides popup
                self.app.main.click_allow_all()
                # print("closed cookie")
            except:
                pass
            # here main functionality is implemented
            widget = str(widget)
            WIDGET_ELEMENT = (By.XPATH, f'//widget[@widgetid = "{widget}"]')
            widget_element = self.app.base.find_clickable_element(WIDGET_ELEMENT, 0)
            # self.app.driver.save_screenshot('screenshot2.png')
            time.sleep(0.1)
            # scrolling to element and then up a bit to position element close to middle of the page
            self.app.main.scroll_to_element(widget_element)
            self.app.main.scroll_up_200()
            time.sleep(0.2)
            widget_id = self.app.main.get_widget_id()
            time.sleep(0.1)

            # print("widget_id - ", widget_id)
            try:
                # test object wrapped into shadow root, so we have to use CSS selectors
                SHADOW_HOST = (By.XPATH, f'//widget[@widgetid = "{widget}"]')
                shadow_host = self.app.base.find_clickable_element(SHADOW_HOST, 0)
                shadow_root = self.app.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
                # print(shadow_root)
                time.sleep(0.2)
                try:
                    widget_opener = shadow_root.find_element(By.CSS_SELECTOR, '#widget_opener')
                    widget_opener.click()
                except:
                    time.sleep(3)
                    # if widget is under some other elements test tries to close it and make another attempt
                    self.app.main.click_esc()
                    time.sleep(0.2)
                    widget_opener = shadow_root.find_element(By.CSS_SELECTOR, '#widget_opener')
                    widget_opener.click()

                time.sleep(0.2)
                # self.app.driver.get_screenshot_as_file('shot.png')
                property_filter = shadow_root.find_element(By.CSS_SELECTOR, '#outer_property_filter')
                property_filter.click()

                time.sleep(0.2)
                #
                filter_first_option = shadow_root.find_element(By.CSS_SELECTOR, '#property_filter_first_option').text
                # assert '0' != filter_first_option
                if filter_first_option != '':
                    try:
                        time.sleep(0.3)
                        self.app.main.click_esc()
                        time.sleep(1)
                        continue_to_checkout = shadow_root.find_element(By.CSS_SELECTOR, '#continue_to_checkout')
                        continue_to_checkout.click()
                        health = "0"
                    except:
                        health = "4"
                else:
                    health = "1"
                # print(health)

                self.app.driver.close()
                time.sleep(0.2)
            except:
                # finally get status - false
                health = "1"
                # print(health)
                self.app.driver.close()
                time.sleep(0.2)
        except:
            widget_id = "can't reach widget"
            health = "2"

        result = [widget_id, health]
        # print("result -", result)
        return result


    def scrape_main_screen_by_url(self, url, widget):
        try:
            self.app.go_to(url)
            return self.scrape_main_screen(widget)
        except:
            result = ["can't reach site", "3"]
            return result