import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


@pytest.fixture
def browser_mozilla():
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    browser.maximize_window()
    yield browser
    browser.quit()
