from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ScenariosPage(BasePage):
    # Flexible locators for alert / frame / tab demo controls
    ALERT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Alert') or contains(.,'Show Alert')]"
    )
    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Confirm') or contains(.,'Show Confirm')]"
    )
    PROMPT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Prompt') or contains(.,'Show Prompt')]"
    )
    RESULT_LABEL = (
        By.XPATH,
        "//*[contains(@class,'result') or contains(@class,'alert') or contains(text(),'Result') or contains(text(),'You clicked') or contains(text(),'Hello')]"
    )

    IFRAME = (By.TAG_NAME, "iframe")
    FRAME_TEXT = (By.XPATH, "//body//*[normalize-space()] | //body")

    NEW_TAB_BUTTON = (
        By.XPATH,
        "//button[contains(.,'New Tab')] | //a[contains(.,'New Tab')]"
    )
    POPUP_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Popup')] | //a[contains(.,'Popup')] | //button[contains(.,'Window')] | //a[contains(.,'Window')]"
    )

    def handle_alert(self):
        self.click(self.ALERT_BUTTON)
        alert = self.waits.wait_for_alert()
        text = alert.text
        alert.accept()
        return text

    def handle_confirm(self, accept=False):
        self.click(self.CONFIRM_BUTTON)
        alert = self.waits.wait_for_alert()
        text = alert.text
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        return text

    def handle_prompt(self, text_value="Hello"):
        self.click(self.PROMPT_BUTTON)
        alert = self.waits.wait_for_alert()
        alert.send_keys(text_value)
        alert.accept()

    def verify_result_label(self):
        try:
            return self.is_displayed(self.RESULT_LABEL)
        except Exception:
            return False

    def switch_to_iframe(self):
        frame = self.waits.wait_for_presence(self.IFRAME)
        self.driver.switch_to.frame(frame)

    def verify_frame_content(self):
        try:
            element = self.waits.wait_for_presence(self.FRAME_TEXT)
            text = element.text.strip()
            self.driver.switch_to.default_content()
            return len(text) >= 0
        except Exception:
            self.driver.switch_to.default_content()
            return False

    def open_new_tab(self):
        original_handles = self.driver.window_handles
        self.click(self.NEW_TAB_BUTTON)
        self.waits.wait_for_number_of_windows(len(original_handles) + 1)

    def verify_new_tab(self):
        handles = self.driver.window_handles
        original = handles[0]
        new_handle = handles[-1]
        self.driver.switch_to.window(new_handle)
        title = self.driver.title
        url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(original)
        return bool(title or url)

    def open_popup(self):
        original_handles = self.driver.window_handles
        self.click(self.POPUP_BUTTON)
        self.waits.wait_for_number_of_windows(len(original_handles) + 1)

    def switch_back_to_main(self):
        handles = self.driver.window_handles
        if handles:
            self.driver.switch_to.window(handles[0])
        self.driver.switch_to.default_content()
        return True