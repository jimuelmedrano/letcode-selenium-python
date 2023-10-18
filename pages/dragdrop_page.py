from selenium.webdriver.common.by import By


class DragDropLocators:
    dragdrop_page_link = (By.XPATH, "//a[@href='/dropable']")
    dragdrop_header = (By.XPATH, "//p[normalize-space()='Drop']")
    draggable_div = "draggable"
    droppble_div = "droppable"

