import os
import time

from selenium.webdriver.common.by import By

from pages.frame_page import FrameLocators
from utils.page_actions import PageActions
from dotenv import load_dotenv


class TestFrame(PageActions):
    def test_open_frame_page(self):
        load_dotenv()
        self.open_page(os.getenv('BASE_URL'))
        self.scroll_to_element(*FrameLocators.frame_header)
        self.click(*FrameLocators.frame_page_link)
        print("Test Letcode Frame")

    def test_input_full_name(self):
        time.sleep(1)
        self.switch_frame(*FrameLocators.first_frame)
        self.input_text(*FrameLocators.first_name_input, "Jimuel Renzo")
        self.input_text(*FrameLocators.last_name_input, "Medrano")

    def test_input_email(self):
        self.switch_frame(*FrameLocators.inner_frame)
        self.input_text(*FrameLocators.email_input, "test@email.com")
