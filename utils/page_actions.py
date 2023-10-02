from selenium.webdriver.common.by import By


class PageActions:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click(self, by, element):
        self.driver.find_element(by, element).click()

    def input_text(self, by, element, text):
        self.driver.find_element(by, element).send_keys(text)

