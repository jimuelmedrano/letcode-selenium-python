from selenium.webdriver.common.by import By


class FrameLocators:
    frame_page_link = (By.XPATH, "//a[@href='/frame']")
    frame_header = (By.XPATH, "//p[normalize-space()='Frame']")
    first_frame = (By.ID, "firstFr")
    inner_frame = (By.XPATH, "//iframe[@src='innerFrame']")
    first_name_input = (By.NAME, "fname")
    last_name_input = (By.NAME, "lname")
    email_input = (By.NAME, "email")

