import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from Library.config import Configuration
from Library.excel_lib import ReadExcel
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class FlightModule:
    obj_1 = ReadExcel()
    locator_fl = obj_1.read_locator(Configuration.FLIGHT_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def oneway_trip_from_textfield_btn(self):
        time.sleep(5)
        locator = self.locator_fl["oneway_trip_from_textfield_btn"]
        self.driver.find_element(*locator).click()

    def from_textfield(self, from_txt):
        time.sleep(2)
        locator = self.locator_fl["from_text_field"]
        self.driver.find_element(*locator).send_keys(from_txt)

    def oneway_trip_from_dropdown(self):
        time.sleep(2)
        locator = self.locator_fl["oneway_trip_from_dropdown"]
        self.driver.find_element(*locator).click()

    def to_textfield(self, to_txt):
        time.sleep(2)
        locator = self.locator_fl["to_text_field"]
        self.driver.find_element(*locator).send_keys(to_txt)

    def oneway_trip_To_dropdown(self):
        time.sleep(2)
        locator = self.locator_fl["oneway_trip_To_dropdown"]
        self.driver.find_element(*locator).click()

    def departure_date(self):
        time.sleep(2)
        locator = self.locator_fl["deaparture_date"]
        self.driver.find_element(*locator).click()

    def oneway_trip_departure_date_done_btn(self):
        time.sleep(2)
        locator = self.locator_fl["deaparture_date_done_btn"]
        self.driver.find_element(*locator).click()

    def adult_btn(self):
        time.sleep(2)
        locator = self.locator_fl["adult_increase_btn"]
        self.driver.find_element(*locator).click()

    def children_btn(self):
        time.sleep(2)
        locator = self.locator_fl["children_increase_btn"]
        self.driver.find_element(*locator).click()

    def infants_btn(self):
        time.sleep(2)
        locator = self.locator_fl["infants_increase_btn"]
        self.driver.find_element(*locator).click()

    def economy_premium_btn(self):
        time.sleep(2)
        locator = self.locator_fl["premium_economy_btn"]
        self.driver.find_element(*locator).click()

    def travellers_class_click_done_btn(self):
        time.sleep(2)
        locator = self.locator_fl["click_done_btn"]
        self.driver.find_element(*locator).click()

    def search_flight_btn(self):
        locator = self.locator_fl["search_flight_btn"]
        time.sleep(2)
        wait_ = WebDriverWait(self.driver, 30)
        wait_.until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()
        time.sleep(5)
