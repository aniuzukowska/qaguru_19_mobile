import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


def test_search():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
    with allure.step('Verify content found'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))



