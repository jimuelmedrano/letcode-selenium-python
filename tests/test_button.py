import os
import time
from pages.button_page import ButtonLocators
from utils.page_actions import PageActions
from dotenv import load_dotenv


class TestButton(PageActions):
    def test_open_button_page(self):
        load_dotenv()
        self.open_page(os.getenv('BASE_URL'))
        self.click(*ButtonLocators.button_page_link)
        print("Test Letcode Button")

    def test_button_home(self):
        # Click home button and go back
        self.click(*ButtonLocators.home_button)
        self.back()

    def test_button_location(self):
        # Print button location
        elm_location = self.get_location(*ButtonLocators.location_button)
        print("Button Location: ", elm_location)

    def test_button_color(self):
        # Print button color
        elm_color = self.get_css_value(*ButtonLocators.color_button, 'background-color')
        print("Button Color: ", elm_color)

    def test_button_size(self):
        # Print button size
        elm_size = self.get_size(*ButtonLocators.size_button)
        print("Button Size: ", elm_size)

    def test_button_disabled(self):
        # Check if button is disabled
        if self.check_enabled(*ButtonLocators.disabled_button):
            print("The element is enabled.")
        else:
            print("The element is not enabled.")

    def test_button_hold(self):
        # Click and hold button
        self.click_and_hold(*ButtonLocators.hold_button)
        time.sleep(2)
