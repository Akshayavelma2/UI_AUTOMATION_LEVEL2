from pathlib import Path

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


DEBUG_DIR = Path("reports/debug_html")
DEBUG_DIR.mkdir(parents=True, exist_ok=True)


def test_debug_projects_page(driver):
    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login_page.open_login_page()
    login_page.login_with_demo_admin()
    dashboard.open_projects()

    (DEBUG_DIR / "projects_page_source.html").write_text(
        driver.page_source,
        encoding="utf-8"
    )

    print("\n===== PROJECTS PAGE URL =====")
    print(driver.current_url)
    print("\nSaved: reports/debug_html/projects_page_source.html")

    assert True


def test_debug_tasks_page(driver):
    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login_page.open_login_page()
    login_page.login_with_demo_admin()
    dashboard.open_tasks()

    (DEBUG_DIR / "tasks_page_source.html").write_text(
        driver.page_source,
        encoding="utf-8"
    )

    print("\n===== TASKS PAGE URL =====")
    print(driver.current_url)
    print("\nSaved: reports/debug_html/tasks_page_source.html")

    assert True