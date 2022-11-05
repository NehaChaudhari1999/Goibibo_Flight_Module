import datetime
import time
import pytest
from Library.config import Configuration
from Library.excel_lib import ReadExcel
from POM.flight_module import FlightModule


class TestFlightModule:
    obj = ReadExcel()
    data = obj.read_test_data(Configuration.FLIGHT_TEST_DATASHEET)

    @pytest.mark.parametrize("from_txt, to_txt", data)
    def test_search_flight(self, init_driver, from_txt, to_txt):
        driver = init_driver
        fl = FlightModule(driver)
        fl.oneway_trip_from_textfield_btn()
        fl.from_textfield(from_txt)
        fl.oneway_trip_from_dropdown()
        fl.to_textfield(to_txt)
        fl.oneway_trip_To_dropdown()
        fl.departure_date()
        fl.oneway_trip_departure_date_done_btn()
        fl.adult_btn()
        fl.children_btn()
        fl.infants_btn()
        fl.economy_premium_btn()
        fl.travellers_class_click_done_btn()
        fl.search_flight_btn()

