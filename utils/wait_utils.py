from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import Settings


class WaitUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Settings.EXPLICIT_WAIT)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

    def wait_for_title_contains(self, text):
        return self.wait.until(EC.title_contains(text))

    def wait_for_alert(self):
        return self.wait.until(EC.alert_is_present())

    def wait_for_number_of_windows(self, count):
        return self.wait.until(lambda d: len(d.window_handles) == count)