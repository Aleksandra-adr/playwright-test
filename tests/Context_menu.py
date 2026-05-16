import time
from playwright.sync_api import sync_playwright


def context_menu():
    with sync_playwright() as ad:
        browser = ad.chromium.launch(headless=True)
        tab = browser.new_page()

        tab.goto("https://the-internet.herokuapp.com/")
        time.sleep(1)

        context_menu_link = tab.locator("//a[text()='Context Menu']")
        time.sleep(1)

        assert context_menu_link.text_content() == "Context Menu"
        context_menu_link.click()
        time.sleep(1)

        # найти квадратик
        box = tab.locator("//div[@id='hot-spot']")

        # регистрируем обработчик
        # tab.on('dialog', lambda dialog: dialog.accept())

        # кликнуть правой кнопки мыши
        box.click(button='right')
        time.sleep(15)

context_menu()

