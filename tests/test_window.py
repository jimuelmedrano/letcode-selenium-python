import os
import time

import pytest
from selenium.webdriver.common.by import By

from pages.window_page import WindowLocators
from utils.page_actions import PageActions
from dotenv import load_dotenv


class TestWindow(PageActions):

    # Using pytest fixture with funtion as scope will run at the start of each test
    @pytest.fixture(autouse=True, scope='function')
    def open_window_page(self):
        load_dotenv()
        self.open_page(os.getenv('BASE_URL'))
        self.scroll_to_element(*WindowLocators.window_page_header)
        self.click(*WindowLocators.window_page_link)
        print("Test Letcode Window")

    def test_switch_window(self):
        # Print current window title
        print(self.get_window_title())
        self.click(*WindowLocators.home_page_button)
        # Switch to the new window by comparing the current window handle
        self.switch_window(self.get_window_handle())
        # Print new window title
        print(self.get_window_title())

    def test_print_all_handles(self):
        self.click(*WindowLocators.multi_page_button)
        self.print_window_handles()
