""" Configuration for tests """
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import datetime

base_url = "https://google.co.in"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    """ Browser setup """
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    request.cls.driver.maximize_window()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """ Configure """
    today = datetime.date.today()
    report_path = Path("reports", f"{today.strftime('%Y-%m-%d')}.html")
    config.option.htmlpath = str(report_path)
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    """ Report title """
    report.title = "Test Report"