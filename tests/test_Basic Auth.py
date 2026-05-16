

from conftest import color_element, closing_element
import time
from playwright.sync_api import sync_playwright



def basic_auth():
    # Запускаем Playwright
    with sync_playwright() as ad:
        # Запуск браузера
        browser = ad.chromium.launch(headless=False)
        # создаем контекст с данными
        tab = browser.new_page()

        tab.goto('https://the-internet.herokuapp.com/')
        time.sleep(2)

        # находим строку Basic
        basic_link = tab.locator("//a[text()='Basic Auth']")
        color_element(basic_link, 'red', 'lightcoral')
        time.sleep(1)

        assert basic_link.text_content() == "Basic Auth"
        closing_element(basic_link)

        basic_link.click()
        time.sleep(2)

        current_url = tab.url
        print(f'Текущий URL после клика: {current_url}')


        #href = basic_link.get_attribute('href')
        #print(f'Ссылка ведет на: {href}')

        #base_url = 'https://the-internet.herokuapp.com'
        new_url = 'https://admin:admin@the-internet.herokuapp.com/basic_auth'
        print(f'Новый URL с авторизацией: {new_url}')

        tab.goto(new_url)
        time.sleep(3)

        # проверяем успех
        success = tab.locator('//p[contains(text(), "Congratulations")]')
        color_element(success, 'green', 'lightgreen')
        time.sleep(1)
        assert 'Congratulations' in success.text_content()
        print('Текст содержит слово "Congratulations"!')

        closing_element(success)
        time.sleep(2)
        browser.close()

basic_auth()










