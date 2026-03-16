from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def dump_elements(driver, page_name):
    print(f"\n===== {page_name} URL =====")
    print(driver.current_url)

    print(f"\n===== {page_name} BUTTONS =====")
    buttons = driver.find_elements("xpath", "//button")
    for i, b in enumerate(buttons, 1):
        print(f"{i}. text='{b.text}' type='{b.get_attribute('type')}' class='{b.get_attribute('class')}'")

    print(f"\n===== {page_name} INPUTS =====")
    inputs = driver.find_elements("xpath", "//input")
    for i, el in enumerate(inputs, 1):
        print(
            f"{i}. type='{el.get_attribute('type')}' "
            f"name='{el.get_attribute('name')}' "
            f"id='{el.get_attribute('id')}' "
            f"placeholder='{el.get_attribute('placeholder')}'"
        )

    print(f"\n===== {page_name} TEXTAREAS =====")
    textareas = driver.find_elements("xpath", "//textarea")
    for i, el in enumerate(textareas, 1):
        print(
            f"{i}. name='{el.get_attribute('name')}' "
            f"id='{el.get_attribute('id')}' "
            f"placeholder='{el.get_attribute('placeholder')}'"
        )

    print(f"\n===== {page_name} SELECTS =====")
    selects = driver.find_elements("xpath", "//select")
    for i, el in enumerate(selects, 1):
        print(
            f"{i}. name='{el.get_attribute('name')}' "
            f"id='{el.get_attribute('id')}' "
            f"class='{el.get_attribute('class')}'"
        )

    print(f"\n===== {page_name} HEADINGS =====")
    heads = driver.find_elements("xpath", "//h1 | //h2 | //h3 | //h4")
    for i, h in enumerate(heads, 1):
        print(f"{i}. '{h.text}'")


def test_debug_projects_page(driver):
    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login_page.open_login_page()
    login_page.login_with_demo_admin()
    dashboard.open_projects()

    dump_elements(driver, "PROJECTS")
    assert True


def test_debug_tasks_page(driver):
    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login_page.open_login_page()
    login_page.login_with_demo_admin()
    dashboard.open_tasks()

    dump_elements(driver, "TASKS")
    assert True