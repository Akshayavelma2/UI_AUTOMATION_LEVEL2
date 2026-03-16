from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (
        By.XPATH,
        "//input[@type='email' or contains(@placeholder,'email') or contains(@placeholder,'Email')]"
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password' or contains(@placeholder,'password') or contains(@placeholder,'Password')]"
    )
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and (contains(.,'Sign In') or contains(.,'Login'))]"
    )
    DEMO_ADMIN_BUTTON = (
        By.XPATH,
        "//button[@type='button' and contains(.,'Admin')]"
    )
    DEMO_USER_BUTTON = (
        By.XPATH,
        "//button[@type='button' and contains(.,'User')]"
    )
    ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(@class,'alert') or contains(@class,'error') or contains(@class,'toast') or contains(text(),'Invalid') or contains(text(),'incorrect') or contains(text(),'required')]"
    )
    LOGIN_HEADING = (
        By.XPATH,
        "//h2[contains(.,'Welcome Back')]"
    )


class DashboardLocators:
    PAGE_TITLE = (
        By.XPATH,
        "//h1 | //h2 | //h3"
    )
    USERS_MENU = (
        By.XPATH,
        "//a[contains(.,'Users')] | //button[contains(.,'Users')] | //span[contains(.,'Users')]"
    )
    PROJECTS_MENU = (
        By.XPATH,
        "//a[contains(.,'Projects')] | //button[contains(.,'Projects')] | //span[contains(.,'Projects')]"
    )
    TASKS_MENU = (
        By.XPATH,
        "//a[contains(.,'Tasks')] | //button[contains(.,'Tasks')] | //span[contains(.,'Tasks')]"
    )
    TEST_SCENARIOS_MENU = (
        By.XPATH,
        "//a[contains(.,'Test Scenarios')] | //button[contains(.,'Test Scenarios')] | //span[contains(.,'Test Scenarios')]"
    )
    ACTIVITY_MENU = (
        By.XPATH,
        "//a[contains(.,'Activity')] | //button[contains(.,'Activity')] | //span[contains(.,'Activity')]"
    )


class UsersLocators:
    USERS_TABLE = (By.XPATH, "//table")
    ACCESS_DENIED = (
        By.XPATH,
        "//*[contains(text(),'Access Denied') or contains(text(),'Unauthorized') or contains(text(),'denied')]"
    )


class ProjectsLocators:
    NEW_PROJECT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'New Project') or contains(.,'Create Project') or contains(.,'Add Project')]"
    )
    PROJECT_NAME_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Project') or @name='projectName' or @id='projectName']"
    )
    PROJECT_DESC_INPUT = (
        By.XPATH,
        "//textarea[contains(@placeholder,'Description') or @name='projectDescription' or @id='projectDescription']"
    )
    SAVE_PROJECT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Save') or contains(.,'Create')]"
    )
    SEARCH_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Search') or @name='search']"
    )
    PROJECT_ROW_BY_NAME = "//tr[td[contains(normalize-space(),'{name}')]]"


class TasksLocators:
    TASK_STATUS_DROPDOWN = (
        By.XPATH,
        "//select[@name='status' or @id='status']"
    )
    SAVE_TASK_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Save') or contains(.,'Update')]"
    )
    TASK_ROW_BY_NAME = "//tr[td[contains(normalize-space(),'{name}')]]"
    TASK_STATUS_CELL_BY_NAME = (
        "//tr[td[contains(normalize-space(),'{name}')]]"
        "/td[contains(@class,'status') or @data-testid='status']"
    )


class TestScenarioLocators:
    ALERT_BUTTON = (By.ID, "alert-btn")
    CONFIRM_BUTTON = (By.ID, "confirm-btn")
    PROMPT_BUTTON = (By.ID, "prompt-btn")
    RESULT_LABEL = (By.ID, "result")
    IFRAME = (By.CSS_SELECTOR, "iframe")
    FRAME_TEXT = (By.CSS_SELECTOR, "body")
    NEW_TAB_BUTTON = (By.ID, "new-tab-btn")
    POPUP_BUTTON = (By.ID, "popup-btn")