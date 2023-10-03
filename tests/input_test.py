import os

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.input_page import InputLocators
from utils.page_actions import PageActions
from dotenv import load_dotenv


@pytest.fixture()
def driver():
    # install chromedriver
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # add implicit wait. It will wait 10 seconds for an element before throwing an error
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_input(driver):
    load_dotenv()
    action = PageActions(driver)
    action.open_page(os.getenv('BASE_URL'))

    print("Test Letcode Input")

    # Input Full Name
    action.click(*InputLocators.input_page_button)
    action.input_text(*InputLocators.full_name_input, "Jimuel Renzo Medrano")

    # Input Skill
    action.input_text(*InputLocators.skill_input, " at Automation")

    # Get Input Value
    input_text = action.get_value(*InputLocators.get_text_input)
    print("Text inside input: " + input_text)

    # Clear Text
    action.clear_text(*InputLocators.clear_text_input)

    # Check Disabled
    if action.check_enabled(*InputLocators.disabled_input):
        print("The element is enabled.")
    else:
        print("The element is not enabled.")

    # Check Readonly
    if action.check_readonly(*InputLocators.readonly_input):
        print("The element is readonly.")
    else:
        print("The element is editable.")
