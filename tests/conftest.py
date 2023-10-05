import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv


# Note that this file should be at the same folder as test files
@pytest.fixture(autouse=True, scope='class')
def setup(request):
    load_dotenv()

    # Set headless mode
    options = Options()
    if os.getenv('HEADLESS') == "Y":
        options.add_argument('--headless')

    # Install chromedriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # Add implicit wait. It will wait 10 seconds for an element before throwing an error
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
