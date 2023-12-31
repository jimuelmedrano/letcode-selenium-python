from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PageActions:

    def open_page(self, url):
        self.driver.get(url)

    def get_element(self, by, element):
        return self.driver.find_element(by, element)

    def scroll_to_element(self, by, element):
        elm = self.driver.find_element(by, element)
        self.driver.execute_script("arguments[0].scrollIntoView();", elm)

    def click(self, by, element):
        self.driver.find_element(by, element).click()

    def click_and_hold(self, by, element):
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

    def get_text(self, by, element):
        return self.driver.find_element(by, element).text

    def clear_text(self, by, element):
        self.driver.find_element(by, element).clear()

    def check_enabled(self, by, element):
        return self.driver.find_element(by, element).is_enabled()

    def check_readonly(self, by, element):
        return self.driver.find_element(by, element).get_attribute('value')

    def back(self):
        self.driver.back()

    def get_location(self, by, element):
        return self.driver.find_element(by, element).location

    def get_size(self, by, element):
        return self.driver.find_element(by, element).size

    def get_css_value(self, by, element, css):
        return self.driver.find_element(by, element).value_of_css_property(css)

    def select_by_visible_text(self, by, element, text):
        select = Select(self.driver.find_element(by, element))
        select.select_by_visible_text(text)

    def select_by_index(self, by, element, index):
        select = Select(self.driver.find_element(by, element))
        select.select_by_index(index)

    def select_by_value(self, by, element, value):
        select = Select(self.driver.find_element(by, element))
        select.select_by_value(value)

    def get_select(self, by, element):
        return Select(self.driver.find_element(by, element))

    def get_alert(self):
        return self.driver.switch_to.alert

    def switch_frame(self, by, element):
        elm = self.driver.find_element(by, element)
        self.driver.switch_to.frame(elm)

    def get_window_title(self):
        return self.driver.title

    def get_window_handle(self):
        return self.driver.current_window_handle

    def print_window_handles(self):
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
            print(self.driver.title)

    def switch_window(self, original_window_handle):
        for window_handle in self.driver.window_handles:
            if window_handle != original_window_handle:
                self.driver.switch_to.window(window_handle)
                break

    def drag_drop(self, by, draggable, droppable):
        source = self.driver.find_element(by, draggable)
        target = self.driver.find_element(by, droppable)
        actions2 = ActionChains(self.driver)
        actions2.drag_and_drop(source, target).perform()
