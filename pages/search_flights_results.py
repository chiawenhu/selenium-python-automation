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
from utilities.utils import Utils

class SearchResults(BaseDriver):
    log = Utils.custom_Logger(logLevel=logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait


    #Locators
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"


    def get_filter_by_one_stop(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.FILTER_BY_1_STOP_ICON)
    
    def get_filter_by_two_stop(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.FILTER_BY_2_STOP_ICON)
    
    def get_filter_by_non_stop(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.FILTER_BY_NON_STOP_ICON)
    

    def get_search_flight_results(self):
        return self.wait_for_presense_of_all_element(By.XPATH, self.SEARCH_FLIGHT_RESULTS)
    
    def filter_flights_by_stop(self, by_stop):
        if by_stop == '1 Stop':
            self.get_filter_by_one_stop().click()
            self.log.warning('Filter by 1 Stop')
            time.sleep(2)
        elif by_stop == '2 Stops':
            self.get_filter_by_two_stop().click()
            self.log.warning('Filter by 2 Stops')
            time.sleep(2)
        elif by_stop == 'Non Stop':
            self.get_filter_by_non_stop().click()
            self.log.warning('Filter by Non Stop')
            time.sleep(2)
        else:
            self.log.warning('Invalid Filter')
