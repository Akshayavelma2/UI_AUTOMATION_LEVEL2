from config.locators import DashboardLocators
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def wait_for_dashboard(self):
        self.waits.wait_for_url_contains("/")
        return (
            self.is_displayed(DashboardLocators.USERS_MENU)
            or self.is_displayed(DashboardLocators.PROJECTS_MENU)
            or self.is_displayed(DashboardLocators.TASKS_MENU)
        )

    def get_page_heading(self):
        return self.get_text(DashboardLocators.PAGE_TITLE)

    def open_users(self):
        self.click(DashboardLocators.USERS_MENU)

    def open_projects(self):
        self.click(DashboardLocators.PROJECTS_MENU)

    def open_tasks(self):
        self.click(DashboardLocators.TASKS_MENU)

    def open_test_scenarios(self):
        self.click(DashboardLocators.TEST_SCENARIOS_MENU)

    def open_activity(self):
        self.click(DashboardLocators.ACTIVITY_MENU)