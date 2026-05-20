

# import pytest
# import allure
# from playwright.sync_api import sync_playwright
#
# @pytest.fixture()
# def main_tab():
#     with sync_playwright() as ad:
#         browser = ad.chromium.launch(headless=True)
#         tab = browser.new_page()
#         tab.goto("https://the-internet.herokuapp.com/")
#         tab.wait_for_load_state('networkidle')
#         yield tab
#         browser.close()
#
#
# @pytest.fixture()
# def geo():
#     with sync_playwright() as ad:
#         browser = ad.chromium.launch(headless=True)
#         context = browser.new_context(
#             permissions=['geolocation'],
#             geolocation={'latitude': 40.712776, 'longitude': -74.005974}
#         )
#         tab = context.new_page()
#         tab.goto("https://the-internet.herokuapp.com/")
#         tab.wait_for_load_state('networkidle')
#         yield  tab
#         browser.close()
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == 'call' and report.failed:
#         # Получаем обьект page из фикстуры (main_tab или geo)
#         page = item.funcargs.get('main_tab') or item.funcargs.get('geo')
#         if page:
#             screenshot = page.screenshot()
#             allure.attach(screenshot, name = 'screenshot_on_failure', attachment_type=allure.attachment_type.PNG)
