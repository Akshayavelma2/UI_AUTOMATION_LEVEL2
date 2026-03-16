from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class TasksPage(BasePage):
    STATUS_DROPDOWN = (
        By.XPATH,
        "(//select[contains(@name,'status') or contains(@id,'status')])[1]"
    )
    SAVE_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Save') or contains(.,'Update') or contains(.,'Submit')]"
    )
    FIRST_TASK_ROW = (
        By.XPATH,
        "(//tr[.//select] | //div[.//select])[1]"
    )

    def update_first_available_task_status(self, new_status):
        self.waits.wait_for_visibility(self.FIRST_TASK_ROW)
        dropdown = self.waits.wait_for_visibility(self.STATUS_DROPDOWN)
        Select(dropdown).select_by_value(new_status)
        self.click(self.SAVE_BUTTON)

    def verify_any_task_has_status(self, expected_status):
        locator = (
            By.XPATH,
            f"//*[contains(translate(normalize-space(), "
            f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
            f"'{expected_status.lower().replace('_', ' ')}') "
            f"or contains(translate(normalize-space(), "
            f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
            f"'{expected_status.lower()}')]"
        )
        return self.is_displayed(locator)