from selenium.webdriver.common.by import By


class WindowLocators:
    window_page_link = (By.XPATH, "//a[@href='/windows']")
    window_page_header = (By.XPATH, "//p[normalize-space()='Window']")
    home_page_button = (By.ID, "home")
    multi_page_button = (By.ID, "multi")

