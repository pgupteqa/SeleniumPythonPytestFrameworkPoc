import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from simple_salesforce import Salesforce
from dotenv import load_dotenv
load_dotenv()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to use")

@pytest.fixture(scope="function")
def browser_setup(request):
    #global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        print("Browser must be 'chrome' or 'firefox' or 'edge'")

    request.cls.driver = driver

    driver.maximize_window()
    driver.get(os.getenv("INSTANCE_URL"))
    driver.implicitly_wait(10)

    yield driver

    #close the browser
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