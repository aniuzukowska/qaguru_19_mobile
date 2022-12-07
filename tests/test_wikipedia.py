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


def test_open_settings():
    with allure.step('Открываем меню действий'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/menu_overflow_button")).click()
    with allure.step('Выбираем в меню пункт Settings'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/explore_overflow_settings")).click()

    with allure.step('Проверяем, что открылась страница Settings'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).\
            element_by(have.text('Settings')).should(be.visible)







