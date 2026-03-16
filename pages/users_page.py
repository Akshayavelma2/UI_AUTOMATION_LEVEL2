from config.locators import UsersLocators
from pages.base_page import BasePage


class UsersPage(BasePage):
    def is_users_table_visible(self):
        return self.is_displayed(UsersLocators.USERS_TABLE)

    def is_access_denied_visible(self):
        return self.is_displayed(UsersLocators.ACCESS_DENIED)