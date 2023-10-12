import os
import time
import unittest

import pytest

from pages.alert_page import AlertLocators
from utils.page_actions import PageActions
from dotenv import load_dotenv


class TestAlert(PageActions):

    @pytest.fixture(autouse=True, scope='function')
    def open_alert_page(self):
        load_dotenv()
        self.open_page(os.getenv('BASE_URL'))
        self.click(*AlertLocators.alert_page_link)
        print("Test Letcode Alert")

    def test_accept_alert(self):
        self.click(*AlertLocators.accept_alert_button)
        alert = self.get_alert()
        alert.accept()

    def test_print_and_dismiss(self):
        self.click(*AlertLocators.confirm_alert_button)
        alert = self.get_alert()
        print(alert.text)
        alert.dismiss()

    def test_prompt_alert(self):
        name = "Renzo"
        self.click(*AlertLocators.prompt_alert_button)
        alert = self.get_alert()
        alert.send_keys(name)
        alert.accept()
        name_text = self.get_text(*AlertLocators.prompt_alert_text)

        assert name in name_text

    def test_modern_alert(self):
        self.click(*AlertLocators.modern_alert_button)
        self.click(*AlertLocators.modern_alert_exit)
