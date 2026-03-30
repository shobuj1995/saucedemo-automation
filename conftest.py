import pytest
from playwright.sync_api import sync_playwright
import platform

# Optional: for dynamic screen size detection on Windows
if platform.system() == "Windows":
    import ctypes


    def get_screen_size():
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
else:
    # Default fallback for Mac/Linux
    def get_screen_size():
        return 1920, 1080  # Replace with your actual screen size if needed


@pytest.fixture(scope="session")
def browser():
    screen_width, screen_height = get_screen_size()
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[f"--window-size={screen_width},{screen_height}", "--start-maximized"]
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    screen_width, screen_height = get_screen_size()

    # Create context without restricting viewport
    context = browser.new_context(
        viewport={"width": screen_width, "height": screen_height},
        screen={"width": screen_width, "height": screen_height}
    )

    page = context.new_page()

    # Force window to occupy full screen using JS (ensures no shrink)
    page.evaluate(
        f"window.moveTo(0,0); window.resizeTo({screen_width},{screen_height});"
    )

    yield page
    context.close()