from utils.wait_utils import WaitUtils


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.waits = WaitUtils(driver)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.waits.wait_for_clickable(locator).click()

    def type(self, locator, text):
        element = self.waits.wait_for_visibility(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.waits.wait_for_visibility(locator).text

    def is_displayed(self, locator):
        try:
            return self.waits.wait_for_visibility(locator).is_displayed()
        except Exception:
            return False

    def current_url(self):
        return self.driver.current_url

    def current_title(self):
        return self.driver.title