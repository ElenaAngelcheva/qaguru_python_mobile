import allure
from allure_commons._allure import step
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

@allure.tag("mobile")
@allure.label('owner', 'Elena')
@allure.severity(Severity.CRITICAL)
@allure.title('Wikipedia search BrowserStack')
def test_search():
    with step('Search for content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")

    with step('Content should be found'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))



@allure.tag("mobile")
@allure.label('owner', 'Elena')
@allure.severity(Severity.CRITICAL)
@allure.title('Open Wikipedia')
def test_open_wikipedia():

    with step('Search for content'):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.LinearLayout")).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.EditText")).type("Wikipedia")

    with step('Content should be found'):
        browser.all((AppiumBy.CLASS_NAME, "android.view.View")).should(have.size_greater_than(0))

