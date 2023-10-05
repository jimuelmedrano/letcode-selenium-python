from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PageActions:

    def open_page(self, url):
        self.driver.get(url)

    def click(self, by, element):
        self.driver.find_element(by, element).click()

    def clickAndHold(self, by, element):
        elm = self.driver.find_element(by, element)
        # create action chain object
        action = ActionChains(self.driver)

        # click and hold  the item
        action.click_and_hold(on_element=elm)

        # perform the operation
        action.perform()

    def input_text(self, by, element, text):
        self.driver.find_element(by, element).send_keys(text)

    def get_value(self, by, element):
        return self.driver.find_element(by, element).get_attribute('value')

    def clear_text(self, by, element):
        self.driver.find_element(by, element).clear()

    def check_enabled(self, by, element):
        return self.driver.find_element(by, element).is_enabled()

    def check_readonly(self, by, element):
        return self.driver.find_element(by, element).get_attribute('value')

    def back(self):
        self.driver.back()

    def getLocation(self, by, element):
        return self.driver.find_element(by, element).location

    def getSize(self, by, element):
        return self.driver.find_element(by, element).size

    def getCssValue(self, by, element, css):
        return self.driver.find_element(by, element).value_of_css_property(css)
