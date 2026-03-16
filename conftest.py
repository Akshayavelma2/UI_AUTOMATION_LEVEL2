import os
import pytest
import allure

from utils.driver_factory import DriverFactory
from utils.data_loader import load_test_data
from utils.logger import get_logger
from utils.screenshot_utils import capture_screenshot


@pytest.fixture(scope="session")
def test_data():
    return load_test_data()


@pytest.fixture(scope="session")
def logger():
    return get_logger("ui_automation")


@pytest.fixture(scope="function")
def driver(logger):
    logger.info("Starting remote browser session")
    driver = DriverFactory.get_driver()
    yield driver
    logger.info("Closing browser session")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            path = capture_screenshot(driver, item.name)
            if os.path.exists(path):
                with open(path, "rb") as file:
                    allure.attach(
                        file.read(),
                        name=f"{item.name}_failure",
                        attachment_type=allure.attachment_type.PNG
                    )