import allure
import allure_commons
from appium import webdriver

import utils.attach
import pytest
from mobile_tests import config
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support


@pytest.fixture(scope='function')
def android_mobile():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23 Ultra",

        # Set URL of the application under test
        "app": "bs://85132b525af9bee5057849aa0cfeec1a73d54664",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Android tests",
            "buildName": "browserstack-wikipedia",
            "sessionName": "wikipedia_test",

            # Set your access credentials
            "userName": config.username,
            "accessKey": config.access_key
        }
    })

    browser.config.driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub",
        options=options
    )
    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield
    utils.attach.attach_bstack_screenshot()
    utils.attach.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.attach.attach_bstack_video(session_id)


@pytest.fixture(scope='function')
def ios_mobile():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "ios",
        "platformVersion": "16",
        "deviceName": "iPhone 14",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "IOS Tests",
            "buildName": "browserstack",
            "sessionName": "Simple app test",

            # Set your access credentials
            "userName": config.username,
            "accessKey": config.access_key
        }
    })

    browser.config.driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub",
        options=options
    )
    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    utils.attach.attach_bstack_screenshot()
    utils.attach.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.attach.attach_bstack_video(session_id)


