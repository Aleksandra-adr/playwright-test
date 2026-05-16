import time
from playwright.sync_api import sync_playwright


def checkboxes_r():
    with sync_playwright() as ad:
        browser = ad.chromium.launch(headless=False)
        tab = browser.new_page()

        tab.goto("https://the-internet.herokuapp.com/")
        time.sleep(1)

        checkboxes_link = tab.locator('//a[text()="Checkboxes"]')
        time.sleep(1)

        assert checkboxes_link.text_content() == "Checkboxes"
        checkboxes_link.click()
        time.sleep(1)

# определить что на странице 2 чекбокса
        check_boxes = tab.locator("input[type='checkbox']") # Находим ВСЕ чекбоксы
        for i in range(check_boxes.count()): # Перебираем все чекбоксы
            if check_boxes.nth(i).is_checked(): # находим включен ли текущий чекбокс
                print(f"Включенный чекбокс - номер {i+1}") # если нашли - выводим
                check_boxes.nth(i).click() # и кликаем по нему изменить состояние
                print(f"Теперь чекбокс включен: {check_boxes.nth(i).is_checked()}")

                break

        else:
            print(f"Включенных чекбоксов не найдено")

            time.sleep(2)


        count = check_boxes.count()
        print(f"На странице : {count} чекбокса")

checkboxes_r()