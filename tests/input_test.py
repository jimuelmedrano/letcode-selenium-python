import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.input_page import InputLocators
from utils.page_actions import PageActions


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_input_full_name(driver):
    action = PageActions(driver)
    action.open_page("https://letcode.in/test")
    action.click(*InputLocators.input_page_button)
    action.input_text(*InputLocators.full_name_input, "Jimuel Renzo Medrano")
    time.sleep(2)

def test_input_skill(driver):
    action = PageActions(driver)
    action.open_page("https://letcode.in/test")
    action.click(*InputLocators.input_page_button)
    action.input_text(*InputLocators.skill_input, " at Automation")
    time.sleep(2)