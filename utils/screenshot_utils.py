import os
from datetime import datetime
from config.settings import Settings


def capture_screenshot(driver, name_prefix="failure"):
    os.makedirs(Settings.SCREENSHOT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(Settings.SCREENSHOT_DIR, f"{name_prefix}_{timestamp}.png")
    driver.save_screenshot(path)
    return path