import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import WebDriverException
from simple_salesforce import Salesforce
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

load_dotenv()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to use")

@pytest.fixture()
def browser_setup(request):
    global driver
    browser_name = request.config.getoption("browser")
    driver = None
    try:
        if browser_name == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        elif browser_name == "edge":
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            pytest.fail("Unsupported browser: choose 'chrome', 'firefox' or 'edge'")

        request.cls.driver = driver

        driver.maximize_window()
        driver.get(os.getenv("INSTANCE_URL"))
        driver.implicitly_wait(10)
        yield driver

    except Exception as e:
        pytest.fail(f"WebDriver setup failed: {str(e)}")

    #close the browser
    finally:
        if driver:
            driver.quit()


'''Fixture to generate and attach screenshot on failure in allure report'''
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    driver = getattr(request.cls, "driver", None)
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


# Attach result of test to node for screenshot
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep