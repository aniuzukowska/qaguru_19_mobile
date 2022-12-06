import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from utils.attach import attach_video
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    load_dotenv()
    username = os.getenv('userName')
    accesskey = os.getenv('accessKey')
    app = os.getenv('app')

    options = UiAutomator2Options().load_capabilities({
        "platformName" : "android",
        "platformVersion" : "9.0",
        "deviceName" : "Google Pixel 3",
        "app" : app,
        'bstack:options' : {
            "projectName" : "First Python project",
            "buildName" : "browserstack-build-1",
            "sessionName" : "BStack first_test",
            "userName" : username,
            "accessKey" : accesskey
        }
    })
    browser.config.driver = webdriver.Remote('http://hub.browserstack.com/wd/hub', options=options)
    yield
    attach_video(browser)
    browser.quit()


