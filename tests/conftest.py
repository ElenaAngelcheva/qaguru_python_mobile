import pytest
from allure_commons._allure import step
from selene.support.shared import browser
from appium import webdriver
from config import options, remote_url


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    with step('Open driver'):
        browser.config.driver = webdriver.Remote(remote_url, options=options)
    yield

    with step('Close driver'):
        browser.quit()

