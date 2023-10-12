from selenium.webdriver.common.by import By


class AlertLocators:
    alert_page_link = (By.XPATH, "//a[@href='/alert']")
    accept_alert_button = (By.ID, "accept")
    confirm_alert_button = (By.ID, "confirm")
    prompt_alert_button = (By.ID, "prompt")
    prompt_alert_text = (By.ID, "myName")
    modern_alert_button = (By.ID, "modern")
    modern_alert_exit = (By.XPATH, "//button[@aria-label='close']")

