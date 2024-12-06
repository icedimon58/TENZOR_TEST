import os
import pytest
from selenium import webdriver
from data import PAGE_URL, PLUGIN_NAME


@pytest.fixture
def page_driver():
    options = webdriver.ChromeOptions()
    options.enable_downloads = True
    options.add_argument('window-size=1920,1080')
    prefs = {
        "download.default_directory": os.getcwd(),
        "download.prompt_for_download": False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get(PAGE_URL)
    yield driver
    driver.quit()
    if os.path.exists(PLUGIN_NAME):
        os.remove(PLUGIN_NAME)
