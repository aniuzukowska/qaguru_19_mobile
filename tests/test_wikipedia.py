import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.conditions import be
from selene.support.shared import browser


def test_search_browserstack():
    with allure.step('Выполняем поиск'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
    with allure.step('Выполняем проверку результатов поиска'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


def test_logo():
    with allure.step('Проверяем наличие логотипа WikipediA'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/single_fragment_toolbar_wordmark")).should(be.existing)



