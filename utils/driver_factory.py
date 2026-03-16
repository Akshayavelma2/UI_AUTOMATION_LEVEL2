from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver
from config.settings import Settings


class DriverFactory:
    @staticmethod
    def _chrome_options():
        options = ChromeOptions()
        if Settings.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return options

    @staticmethod
    def _edge_options():
        options = EdgeOptions()
        if Settings.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return options

    @staticmethod
    def get_driver() -> WebDriver:
        browser = Settings.BROWSER

        if browser == "chrome":
            options = DriverFactory._chrome_options()
        elif browser == "edge":
            options = DriverFactory._edge_options()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver = webdriver.Remote(
            command_executor=Settings.GRID_URL,
            options=options
        )

        driver.implicitly_wait(Settings.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Settings.PAGE_LOAD_TIMEOUT)
        return driver