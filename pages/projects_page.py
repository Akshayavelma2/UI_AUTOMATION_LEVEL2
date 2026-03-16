from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProjectsPage(BasePage):
    NEW_PROJECT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'New Project') or contains(.,'Create Project') or contains(.,'Add Project') or contains(.,'New')]"
    )
    PROJECT_NAME_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Project') "
        "or contains(@placeholder,'project') "
        "or @name='name' "
        "or @name='projectName' "
        "or @id='name' "
        "or @id='projectName']"
    )
    PROJECT_DESC_INPUT = (
        By.XPATH,
        "//textarea[contains(@placeholder,'Description') "
        "or contains(@placeholder,'description') "
        "or @name='description' "
        "or @name='projectDescription' "
        "or @id='description' "
        "or @id='projectDescription']"
    )
    SAVE_PROJECT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Save') or contains(.,'Create') or contains(.,'Submit')]"
    )
    SEARCH_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Search') or contains(@placeholder,'search') or @name='search']"
    )

    def open_create_project_form(self):
        self.click(self.NEW_PROJECT_BUTTON)
        self.waits.wait_for_visibility(self.PROJECT_NAME_INPUT)

    def create_project(self, name, description):
        self.open_create_project_form()
        self.type(self.PROJECT_NAME_INPUT, name)

        if self.is_displayed(self.PROJECT_DESC_INPUT):
            self.type(self.PROJECT_DESC_INPUT, description)

        self.click(self.SAVE_PROJECT_BUTTON)

    def search_project(self, name):
        if self.is_displayed(self.SEARCH_INPUT):
            self.type(self.SEARCH_INPUT, name)

    def verify_project_exists(self, name):
        self.search_project(name)
        result_locator = (
            By.XPATH,
            f"//*[self::tr or self::td or self::div or self::span][contains(normalize-space(),'{name}')]"
        )
        return self.is_displayed(result_locator)