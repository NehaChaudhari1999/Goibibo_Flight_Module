import pytest
from selenium import webdriver
from Library.config import Configuration


@pytest.fixture(params=["Chrome"])
def init_driver(request):  # request is a library

    browser = request.param

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)

    '''elif browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=Configuration.FIREFOX_PATH)

    else:
        driver = webdriver.Edge(executable_path=Configuration.MSEDGE_PATH)'''

    driver.get(Configuration.URL)
    driver.maximize_window()
    yield driver
    # driver.close()
