import time
from playwright.sync_api import sync_playwright

def color_element(element, color = 'red', fon = 'yellow'):
    element.evaluate(f'''
        element => {{
            element.style.border = '3px solid {color}';
            element.style.backgroundColor = '{fon}';
            element.style.transition = '0.3s';
        }}
    ''')

def puc_element(element):
    element.evaluate('''
        element => {
            element.style.border = '';
            element.style.backgroundColor = '';
        }
    ''')


def test_web():
    # Запускаем Playwright
    with sync_playwright() as ad:

        # Запуск браузера
        brauzer = ad.chromium.launch(headless=False)

        # Создание новой вкладки
        vcladka = brauzer.new_page()

        # Открыть страницу
        vcladka.goto('https://the-internet.herokuapp.com/')

        # Слип 1
        time.sleep(2)

        # Проверяем h1
        h1 = vcladka.locator('h1')
        color_element(h1, 'red', 'lightcoral')

        # Слип 2
        time.sleep(1.5)

        h1_text = h1.text_content()

        # Сравнить
        cravnenie_h1 = 'Welcome to the-internet'
        assert h1_text == cravnenie_h1

        # снять подсветку
        puc_element(h1)
        # Слип 3
        time.sleep(0.5)

        # Найти подзаголовок h2
        h2 = vcladka.locator('h2')
        color_element(h2, 'blue', 'lightblue')

        # Слип 4
        time.sleep(1.5)

        # Сравнить
        h2_text = h2.text_content()
        cravnenie_h2 = 'Available Examples'
        assert h2_text == cravnenie_h2

        puc_element(h2)
        # Слип 5
        time.sleep(2)

        brauzer.close()







