from selenium.webdriver.common.by import By


class DropdownLocators:
    dropdown_page_link = (By.XPATH, "//a[@href='/dropdowns']")
    fruits_dropdown = (By.ID, "fruits")
    heroes_dropdown = (By.ID, "superheros")
    language_dropdown = (By.ID, "lang")
    country_dropdown = (By.ID, "country")
