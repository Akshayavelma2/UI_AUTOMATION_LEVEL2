import pytest
import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.locators import DashboardLocators, UsersLocators


@allure.feature("Access Control")
class TestAccessControl:

    @pytest.mark.access
    @allure.title("TC04 - Non Admin Access Restriction")
    def test_non_admin_access_restriction(self, driver, logger):
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)

        logger.info("Login as normal user")
        login_page.open_login_page()
        login_page.login_with_demo_user()

        if dashboard.is_displayed(DashboardLocators.USERS_MENU):
            logger.info("Users menu visible for normal user, checking restriction after click")
            dashboard.open_users()
            assert (
                dashboard.is_displayed(UsersLocators.ACCESS_DENIED)
                or "/users" not in driver.current_url.lower()
            ), "Expected access restriction for non-admin user"
        else:
            logger.info("Users menu hidden for normal user, restriction works")
            assert not dashboard.is_displayed(DashboardLocators.USERS_MENU)