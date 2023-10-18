import os
import time

import pytest
from selenium.webdriver.common.by import By

from pages.dragdrop_page import DragDropLocators
from utils.page_actions import PageActions
from dotenv import load_dotenv


class TestDragDrop(PageActions):

    # Using pytest fixture with funtion as scope will run at the start of each test
    @pytest.fixture(autouse=True, scope='function')
    def open_dragdrop_page(self):
        load_dotenv()
        self.open_page(os.getenv('BASE_URL'))
        self.scroll_to_element(*DragDropLocators.dragdrop_header)
        self.click(*DragDropLocators.dragdrop_page_link)
        print("Test Letcode Drag and Drop")

    def test_switch_window(self):
        self.drag_drop(By.ID, DragDropLocators.draggable_div, DragDropLocators.droppble_div)


