import allure
@allure.feature("Управление элементами")
@allure.story("Добавление и удаление элементов")
@allure.title("Тест Add/Remove Element")
@allure.severity(allure.severity_level.CRITICAL)


from conftest import main_tab
from helpers.visual_helpers import color_element, closing_element
from pages.home_page import HomePage
import time


def test_add_remove_elements_test(main_tab):
    with allure.step("Переход на страницу Add/Remove Element"):
        home = HomePage(main_tab)
        home.go('Add/Remove Elements')

    with allure.step("Проверка заголовка"):
        h3 = main_tab.locator('h3')
        color_element(h3, 'red', 'lightcoral')
        time.sleep(1)
        assert h3.text_content() == "Add/Remove Elements"
        closing_element(h3)

    with allure.step("Проверка кнопки Add element"):
        button_add = main_tab.locator('//button[@onclick="addElement()"]')
        color_element(button_add, 'blue', 'lightblue')
        time.sleep(1.5)
        assert button_add.text_content() == "Add Element"
        closing_element(button_add)

    with allure.step("Добавление 5 элементов"):
        for i in range(5):
            print(f"Нажатие номер {i + 1}")

            button_add.click()
            time.sleep(1)

    with allure.step("Проверка количества кнопок Delete"):
        button_delete = main_tab.locator('//button[@class="added-manually"]')
        assert button_delete.count() == 5

    with allure.step("Удаление 3 элементов"):
        for i in range(3):
            first_delete = button_delete.first
            color_element(first_delete, 'red', 'lightcoral')
            time.sleep(2)
            first_delete.click()
            time.sleep(0.5)

    with allure.step("Проверка окончательного количества кнопок"):
        assert button_delete.count() == 2




#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         tab = browser.new_page()
#         tab.goto('https://the-internet.herokuapp.com/')
#         time.sleep(2)
#
#         # Находим строку Add
#         add_remove_elements_link = tab.locator('//a[text()="Add/Remove Elements"]')
#         color_element(add_remove_elements_link, 'red', 'lightcoral')
#         time.sleep(1)
#
#         add_text = add_remove_elements_link.text_content()
#         assert add_text == "Add/Remove Elements"
#
#         closing_element(add_remove_elements_link)
#
#         # нажимаем на строчку
#         add_remove_elements_link.click()
#
#         # найти и сравнить заголовок
#         h3 = tab.locator('h3')
#         color_element(h3, 'red', 'lightcoral')
#         time.sleep(1)
#
#         h3_text = h3.text_content()
#         assert h3_text == "Add/Remove Elements"
#
#         closing_element(h3)
#
#         # Найти и сравнить подзаголовок
#         button_add = tab.locator('//button[@onclick="addElement()"]')
#         color_element(button_add, 'blue', 'lightblue')
#         time.sleep(1.5)
#
#         button_text = button_add.text_content()
#         assert button_text == "Add Element"
#
#         closing_element(button_add)
#         for i in range(5):
#             print(f"Нажатие номер {i + 1}")
#
#             button_add.click()
#             time.sleep(1)
#
#         # Находим и кликаем на Delete
#         button_delete = tab.locator('//button[@class="added-manually"]')
#         actual_count = button_delete.count()
#         assert actual_count == 5
#
#         for i in range(3):
#             first_delete = tab.locator('//button[@class="added-manually"]').first
#
#             # подсвечиваем перед удалением
#             color_element(first_delete, 'red', 'lightcoral')
#             time.sleep(2)
#
#             # удаляем
#             first_delete.click()
#             time.sleep(0.5)
#
#
#         # проверяем что Delete удалился
#         assert button_delete.count() == 2
#         print("Элемент удален!")
#
#         browser.close()
#
# add_remove_elements_test()




