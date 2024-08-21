import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest
import logging

from base.base_driver import BaseDriver
from pages.search_flights_results import SearchResults
from utilities.utils import Utils

class LaunchPage(BaseDriver):
    log = Utils.custom_Logger(logLevel=logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        time.sleep(5)
        return self.wait_for_presense_of_all_element(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepatureDateField(self):
        time.sleep(5)
        return self.wait_for_presense_of_all_element(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        time.sleep(2)
        self.getDepartFromField().clear()
        time.sleep(2)
        self.getDepartFromField().send_keys(departlocation)
        time.sleep(2)
        self.getDepartFromField().send_keys(Keys.ENTER)
        time.sleep(2)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        self.getGoingToField().send_keys(goingtolocation)
        search_results = self.getGoingToResults()
        for results in search_results:
            if goingtolocation in results.text:
                results.click()
                break

    def enterDepartureDate(self, departuredate):
        self.getDepatureDateField()[0].click()
        all_dates = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        
    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightsButton()
        # we can connect the other page using the trigger here
        searchflight_result = SearchResults(self.driver)
        return searchflight_result
