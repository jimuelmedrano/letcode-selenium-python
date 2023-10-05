from selenium.webdriver.common.by import By


class ButtonLocators:
    button_page_link = (By.XPATH, "//a[@href='/buttons']")
    home_button = (By.ID, "home")
    location_button = (By.ID, "position")
    color_button = (By.ID, "color")
    size_button = (By.ID, "property")
    disabled_button = (By.ID, "isDisabled")
    hold_button = (By.XPATH, "//label[normalize-space()='Click and Hold Button']//following-sibling::div//button")

