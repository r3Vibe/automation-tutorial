""" Test Search """
import pytest
from conftest import base_url
from pages.search_page import SearchPage

@pytest.mark.usefixtures("browser_setup")
class TestSearch:
    """ Test Search """

    def setup_class(self):
        """ Setup Class """
        self.driver.get(base_url)
        self.search_page = SearchPage(self.driver)

    def test_search(self):
        """ Test Search """
        self.search_page.search("What is selenium ?")
        self.search_page.click_element(SearchPage.SEARCH_BUTTON)

    def teardown_class(self):
        """ Teardown Class """
        self.driver.quit()
    