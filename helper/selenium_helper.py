""" Helper Class For Selenium """
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumHelper:
    """ Selenium Helper Class """
    def __init__(self, driver):
        """ Constructor """
        self.driver = driver

    def click_element(self, locator):
        """ Click Element """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """ Enter Text """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
    