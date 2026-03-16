import os


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://react-frontend-api-testing.vercel.app")
    GRID_URL = os.getenv("GRID_URL", "http://localhost:4444")
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "2"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))
    SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "screenshots")
    LOG_DIR = os.getenv("LOG_DIR", "logs")