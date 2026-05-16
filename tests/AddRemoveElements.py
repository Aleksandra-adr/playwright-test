from conftest import main_tab
from helpers.visual_helpers import color_element, closing_element
from pages.AddRemoveElements_page import HomePage


def add_remove_elements_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        tab = browser.new_page()
        tab.goto('https://the-internet.herokuapp.com/')
        time.sleep(2)

        # Находим строку Add
        add_remove_elements_link = tab.locator('//a[text()="Add/Remove Elements"]')
        color_element(add_remove_elements_link, 'red', 'lightcoral')
        time.sleep(1)

        add_text = add_remove_elements_link.text_content()
        assert add_text == "Add/Remove Elements"

        closing_element(add_remove_elements_link)

        # нажимаем на строчку
        add_remove_elements_link.click()

        # найти и сравнить заголовок
        h3 = tab.locator('h3')
        color_element(h3, 'red', 'lightcoral')
        time.sleep(1)

        h3_text = h3.text_content()
        assert h3_text == "Add/Remove Elements"

        closing_element(h3)

        # Найти и сравнить подзаголовок
        button_add = tab.locator('//button[@onclick="addElement()"]')
        color_element(button_add, 'blue', 'lightblue')
        time.sleep(1.5)

        button_text = button_add.text_content()
        assert button_text == "Add Element"

        closing_element(button_add)
        for i in range(5):
            print(f"Нажатие номер {i + 1}")

            button_add.click()
            time.sleep(1)

        # Находим и кликаем на Delete
        button_delete = tab.locator('//button[@class="added-manually"]')
        actual_count = button_delete.count()
        assert actual_count == 5

        for i in range(3):
            first_delete = tab.locator('//button[@class="added-manually"]').first

            # подсвечиваем перед удалением
            color_element(first_delete, 'red', 'lightcoral')
            time.sleep(2)

            # удаляем
            first_delete.click()
            time.sleep(0.5)


        # проверяем что Delete удалился
        assert button_delete.count() == 2
        print("Элемент удален!")

        browser.close()

add_remove_elements_test()




