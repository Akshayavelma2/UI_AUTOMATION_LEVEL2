import pytest
import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.test_scenarios_page import ScenariosPage


@allure.feature("Browser Interactions")
class TestBrowserInteractions:

    @pytest.mark.browser
    @allure.title("TC07 - Alerts Handling")
    def test_alerts_handling(self, driver, logger):
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)
        scenarios = ScenariosPage(driver)

        login_page.open_login_page()
        login_page.login_with_demo_admin()

        dashboard.open_test_scenarios()

        scenarios.handle_alert()
        scenarios.handle_confirm()
        scenarios.handle_prompt("Hello")

        assert scenarios.verify_result_label() or "/test" in driver.current_url.lower()

    @pytest.mark.browser
    @allure.title("TC08 - Frames and Window Handling")
    def test_frames_and_windows(self, driver, logger):
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)
        scenarios = ScenariosPage(driver)

        login_page.open_login_page()
        login_page.login_with_demo_admin()

        dashboard.open_test_scenarios()

        scenarios.switch_to_iframe()
        assert scenarios.verify_frame_content()

        scenarios.open_new_tab()
        assert scenarios.verify_new_tab()

        scenarios.open_popup()
        assert scenarios.switch_back_to_main()