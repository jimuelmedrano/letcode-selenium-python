from selenium.webdriver.common.by import By


class InputLocators:
    input_page_button = (By.XPATH, "//a[@href='/edit']")
    full_name_input = (By.ID, "fullName")
    skill_input = (By.ID, "join")
    get_text_input = (By.ID, "getMe")
    clear_text_input = (By.ID, "clearMe")
    disabled_input = (By.ID, "noEdit")
    readonly_input = (By.ID, "dontwrite")
