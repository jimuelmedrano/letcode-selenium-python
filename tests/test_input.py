import os
import time
from pages.input_page import InputLocators
from utils.page_actions import PageActions
from dotenv import load_dotenv


class TestInput(PageActions):
    def test_open_input_page(self):
        load_dotenv()
        self.open_page(os.getenv('BASE_URL'))
        self.click(*InputLocators.input_page_link)
        print("Test Letcode Input")

    def test_input_full_name(self):
        # Input Full Name
        self.input_text(*InputLocators.full_name_input, "Jimuel Renzo Medrano")

    def test_input_skill(self):
        # Input Skill
        self.input_text(*InputLocators.skill_input, " at Automation")

    def test_input_get_value(self):
        # Get Input Value
        input_text = self.get_value(*InputLocators.get_text_input)
        print("Text inside input: " + input_text)

    def test_input_clear_text(self):
        # Clear Text
        self.clear_text(*InputLocators.clear_text_input)

    def test_input_check_disabled(self):
        # Check Disabled
        if self.check_enabled(*InputLocators.disabled_input):
            print("The element is enabled.")
        else:
            print("The element is not enabled.")

    def test_input_check_readonly(self):
        # Check Readonly
        if self.check_readonly(*InputLocators.readonly_input):
            print("The element is readonly.")
        else:
            print("The element is editable.")
        time.sleep(2)
