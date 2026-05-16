import pytest
from playwright.sync_api import sync_playwright, expect


# @pytest.fixture()
# def main_tab():
#     with sync_playwright() as ad:
#         browser = ad.chromium.launch(headless=False)
#         tab = browser.new_page()
#         tab.goto("https://the-internet.herokuapp.com/")
#         tab.wait_for_load_state('networkidle')
#         yield tab
#         browser.close()


def test_dropdown(main_tab):
    dropdown_link = main_tab.locator("//a[text()= 'Dropdown']")
    assert dropdown_link.text_content() == 'Dropdown'

    dropdown_link.click()
    main_tab.wait_for_load_state('networkidle')

    # Найти дропдаун
    dropdown_list = main_tab.locator("//select[@id='dropdown']")
    dropdown_list.wait_for(state='visible')

    # получить список всех досутпных опций в дропдауне
    options = dropdown_list.locator ("//option[@value>=1]")
    errors = []

    for i in range(options.count()):
        value = options.nth(i).get_attribute('value')
        text = options.nth(i).text_content()

        # пропускаем пустоты
        #if value =='':
         #   continue

    # выбрать пункты в дропдауне
        dropdown_list.select_option(value)
        main_tab.wait_for_timeout(300)

    # проверяем выбранное значение
        selected_value = dropdown_list.input_value()

        # сравниванием
        if selected_value != value:
            errors.append(f"Опция '{text}': выбрано {selected_value}, ожидалось '{value}'")
        else:
            print(f"Успех")


    assert not errors, f'\nНайдено {len(errors)}'




