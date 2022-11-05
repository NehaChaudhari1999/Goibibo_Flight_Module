# path or url are store inthis file all
class Configuration:
    URL = "https://www.goibibo.com/"

    # relative path if u want to share project to teammate
    CHROME_PATH = r"../drivers/chromedriver.exe"


    # FIREFOX_PATH = r'../drivers/geckodriver.exe'
    #
    # MSEDGE_PATH = r"../drivers/msedgedriver.exe"

    LOCATORS_PATH = r'../test_data/locators.xlsx'

    TESTDATA_PATH = r'../test_data/Flight_test_data.xlsx'

    REPORTS_PATH = r"../reportS/"

    SCREENSHOTS_PATH = r"../Screenshots/"
    # gives report and screenshot folder path \\

    FLIGHT_LOCATOR_SHEET = "flight_locator"

    FLIGHT_TEST_DATASHEET = "test_data_flight"
