import time
from conftest import closing_element, color_element
from playwright.sync_api import sync_playwright


def challenging_dom():
    with (sync_playwright() as ad):
        browser = ad.chromium.launch(headless=False)
        tab = browser.new_page()

        tab.goto('https://the-internet.herokuapp.com/')
        time.sleep(1.5)

        challenging_link = tab.locator("//a[text()='Challenging DOM']")
        color_element(challenging_link, 'red', 'lightcoral')
        time.sleep(1)

        assert challenging_link.text_content() == "Challenging DOM"
        closing_element(challenging_link)

        challenging_link.click()
        time.sleep(1)

        # находим кнопки
        buttons = tab.locator("div.large-2.columns a.button")

        count = buttons.count()
        print(f"Найдено кнопок : {count}")

        # выводим текст каждой кнопки ДО нажатия
        for i in range(count):
            print(f"Кнопка {i + 1}: {buttons.nth(i).text_content()}")

        # сохраняем цвет ДО нажатия
        colors_before = []

        for i in range(count):
            button = buttons.nth(i)
            # получаем цвет фона ДО
            color = button.evaluate("el => getComputedStyle(el).backgroundColor")
            colors_before.append(color)
            print(f"Кнопка {i+1}- цвет = {color}")

        # кликаем на каждую кнопку
        for i in range(buttons.count()):
            buttons.nth(i).click()
            time.sleep(1)

        # уводим фокус
        tab.locator('h3').click()
        print(f"фокус убран")

        # выводим цвет и текст ПОСЛЕ клика
        buttons_after = tab.locator("div.large-2.columns a.button")

        for i in range(buttons_after.count()):
            text = buttons_after.nth(i).text_content()
            color = buttons_after.nth(i).evaluate("el => getComputedStyle(el).backgroundColor")
            print(f"Кнопка {i+1}: текст = '{text}', цвет = {color}")

            time.sleep(2)

        # сравниваем цвета ДО и ПОСЛЕ
            if colors_before[i] == color:
                print(f" Кнопка {i+1}: цвет сохранен")
            else:
                print(f"Кнопка: {i+1}: Цвет изменился : было- {colors_before[i]}, стало {color}")
            time.sleep(2)


challenging_dom()



