import playwright.sync_api
from playwright.sync_api import sync_playwright


def drap_and_drop():
    with (sync_playwright() as ad):
        browser = ad.chromium.launch(headless=False)
        tab = browser.new_page()
        tab.goto("https://the-internet.herokuapp.com/")
        tab.wait_for_load_state('networkidle')

        drag_and_drop_link = tab.locator("//a[contains(text(),'Drag')]")
        drag_and_drop_link.wait_for(state='visible', timeout=5000)
        assert drag_and_drop_link.text_content() == "Drag and Drop"

        drag_and_drop_link.click()
        tab.wait_for_load_state('networkidle')

        # найти все картинки
        element_a = tab.locator("#column-a")
        element_b = tab.locator("#column-b")

        # Получаем текста элементов
        text_a = element_a.locator("header").inner_text()
        text_b = element_b.locator("header").inner_text()

        # поменять местами картинки
        element_a.drag_to(element_b)
        tab.wait_for_load_state('networkidle')

        # убедиться, что картинки места изменили
        a_text = element_a.locator('header').text_content()
        b_text = element_b.locator('header').text_content()

        #print(f"A: {a_text}, B: {b_text}")
        assert a_text == text_b and b_text == text_a, "Картинки не поменялись местами"


drap_and_drop()



