from selenium_service_example.src.scraper import Scraper

# this is controller file in case if some manipulation with data is needed
# in that service this function is redundant
def check_site(url, widget):
    scraper = Scraper()
    data = scraper.scrape_main_screen_by_url(url, widget)
    scraper.close()

    return data


