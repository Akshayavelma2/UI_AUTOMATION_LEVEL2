from config.settings import Settings
from config.locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open_login_page(self):
        self.open(f"{Settings.BASE_URL}/login")
        self.waits.wait_for_visibility(LoginLocators.LOGIN_HEADING)

    def login(self, email, password):
        self.type(LoginLocators.EMAIL_INPUT, email)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def login_with_demo_admin(self):
        self.click(LoginLocators.DEMO_ADMIN_BUTTON)
        self.click(LoginLocators.LOGIN_BUTTON)

    def login_with_demo_user(self):
        self.click(LoginLocators.DEMO_USER_BUTTON)
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        try:
            return self.get_text(LoginLocators.ERROR_MESSAGE)
        except Exception:
            return ""

    def get_native_validation_message(self, locator):
        element = self.waits.wait_for_presence(locator)
        return self.driver.execute_script(
            "return arguments[0].validationMessage;", element
        )

    def get_email_validation_message(self):
        return self.get_native_validation_message(LoginLocators.EMAIL_INPUT)

    def get_password_validation_message(self):
        return self.get_native_validation_message(LoginLocators.PASSWORD_INPUT)

    def logout(self):
        pass