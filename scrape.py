import selenium.webdriver as webdriver 
from selenium.webdriver.chrome.service import Service


def scrape_website(website):
    print("Launching chrome browswer...")

    chrome_driver_path = "./chromedriver"
    options = webdriver.VhromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source

        return html
    finally:
        driver.quit()