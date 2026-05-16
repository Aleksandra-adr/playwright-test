import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def main_tab():
    with sync_playwright() as ad:
        browser = ad.chromium.launch(headless=False)
        tab = browser.new_page()
        tab.goto("https://the-internet.herokuapp.com/")
        tab.wait_for_load_state('networkidle')
        yield tab
        browser.close()


@pytest.fixture()
def geo():
    with sync_playwright() as ad:
        browser = ad.chromium.launch(headless=False)
        context = browser.new_context(
            permissions=['geolocation'],
            geolocation={'latitude': 40.712776, 'longitude': -74.005974}
        )
        tab = context.new_page()
        tab.goto("https://the-internet.herokuapp.com/")
        tab.wait_for_load_state('networkidle')
        yield  tab
        browser.close()


