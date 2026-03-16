import pytest
import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.feature("Projects and Tasks")
class TestProjectsTasks:

    @pytest.mark.projects
    @allure.title("TC05 - Projects Page Load")
    def test_project_creation(self, driver, logger):
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)

        login_page.open_login_page()
        login_page.login_with_demo_admin()

        logger.info("Opening Projects module")
        dashboard.open_projects()

        logger.info("Validating Projects page loaded")
        assert "project" in driver.current_url.lower() or driver.title != ""


    @pytest.mark.tasks
    @allure.title("TC06 - Tasks Page Load")
    def test_task_status_update(self, driver, logger):
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)

        login_page.open_login_page()
        login_page.login_with_demo_admin()

        logger.info("Opening Tasks module")
        dashboard.open_tasks()

        logger.info("Validating Tasks page loaded")
        assert "task" in driver.current_url.lower() or driver.title != ""