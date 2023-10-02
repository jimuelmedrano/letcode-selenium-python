from selenium.webdriver.common.by import By


class InputLocators:
    input_page_button = (By.XPATH, "//a[@href='/edit']")
    full_name_input = (By.ID, "fullName")
    skill_input = (By.ID, "join")
