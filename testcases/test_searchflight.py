
import pytest

from pages.yatra_launch_page import LaunchPage

from utilities.utils import Utils
import softest

from ddt import ddt, data, unpack, file_data

@pytest.mark.usefixtures('setup')
@ddt
class Test_SearchAndVerify(softest.TestCase):
    log = Utils.custom_Logger()

    @pytest.fixture(autouse = True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    @file_data("../testdata/testdata.json")
    # @data(Utils.read_data_from_excel("testdata.xlsx", "Sheet1"))
    @unpack
    def test_searchflight_1stop(self, goingfrom, goingto, date, stop):

        search_flights_result = self.lp.searchFlights(goingfrom, goingto, date)
        search_flights_result.filter_flights_by_stop(stop)  
        self.lp.pagescoll()
        allstops = search_flights_result.get_search_flight_results()
        self.log.info('The number of stops are: ' + str(len(allstops)))
        self.ut.assertListItemText(allstops, stop)
