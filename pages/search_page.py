""" Search Page """
from helper.selenium_helper import SeleniumHelper
from selenium.webdriver.common.by import By

class SearchPage(SeleniumHelper):

    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")

    def __init__(self, driver):
        """ Constructor """
        super().__init__(driver)
        self.driver = driver

    def search(self, text):
        """ Search """
        self.enter_text(self.SEARCH_FIELD, text)