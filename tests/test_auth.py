import pytest
import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.locators import LoginLocators, DashboardLocators


@allure.feature("Authentication")
class TestAuth:

    @pytest.mark.auth
    @pytest.mark.smoke
    @allure.title("TC01 - Valid Admin Login")
    def test_valid_admin_login(self, driver, logger):
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)

        logger.info("Opening login page")
        login_page.open_login_page()

        logger.info("Logging in with demo admin button")
        login_page.login_with_demo_admin()

        assert dashboard.wait_for_dashboard(), "Dashboard did not load"
        assert dashboard.is_displayed(DashboardLocators.USERS_MENU)

    @pytest.mark.auth
    @pytest.mark.regression
    @allure.title("TC02 - Invalid Login Matrix")
    @pytest.mark.parametrize(
        "email,password,case_type",
        [
            ("admin@example.com", "WrongPass123", "wrong_password"),
            ("invalid-email-format", "Admin@123", "invalid_email"),
            ("", "", "empty_fields"),
        ],
    )
    def test_invalid_login_matrix(self, driver, email, password, case_type, logger):
        login_page = LoginPage(driver)

        logger.info("Opening login page")
        login_page.open_login_page()
        login_page.login(email, password)

        if case_type == "wrong_password":

            error_text = login_page.get_error_message()

            assert "/login" in driver.current_url
            assert error_text != "" or login_page.is_displayed(LoginLocators.LOGIN_BUTTON)

        elif case_type == "invalid_email":

            validation = login_page.get_email_validation_message()
            assert validation != ""

        elif case_type == "empty_fields":

            validation = login_page.get_email_validation_message()
            assert validation != ""