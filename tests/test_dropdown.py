import os
import time
from pages.dropdown_page import DropdownLocators
from utils.page_actions import PageActions
from dotenv import load_dotenv


class TestDropdown(PageActions):
    def test_open_dropdown_page(self):
        load_dotenv()
        self.open_page(os.getenv('BASE_URL'))
        self.click(*DropdownLocators.dropdown_page_link)
        print("Test Letcode Dropdown")

    def test_select_visible_text(self):
        self.select_by_visible_text(*DropdownLocators.fruits_dropdown, "Apple")

    def test_select_multiple(self):
        self.select_by_visible_text(*DropdownLocators.heroes_dropdown, "Aquaman")
        self.select_by_visible_text(*DropdownLocators.heroes_dropdown, "Ant-Man")
        # Print all selected values
        select = self.get_select(*DropdownLocators.heroes_dropdown)
        selected_options = select.all_selected_options
        for x in selected_options:
            print(x.text)

    def test_print_all_option(self):
        select = self.get_select(*DropdownLocators.language_dropdown)
        options = select.options

        # Print all options
        for x in options:
            print(x.text)

        # Select Last option
        self.select_by_index(*DropdownLocators.language_dropdown, len(options)-1)

    def test_select_value(self):
        self.select_by_value(*DropdownLocators.country_dropdown, "India")
        # Print all selected values
        select = self.get_select(*DropdownLocators.country_dropdown)
        selected_options = select.all_selected_options
        for x in selected_options:
            print(x.text)
