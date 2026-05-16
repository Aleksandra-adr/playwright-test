import time
from conftest import color_element, closing_element
from playwright.sync_api import sync_playwright



def broken_images():
    with sync_playwright() as ad:
        browser = ad.chromium.launch(headless=True)
        tab = browser.new_page()

        tab.goto('https://the-internet.herokuapp.com/')
        time.sleep(1.5)

        broken_link = tab.locator('//a[text()="Broken Images"]')
        color_element(broken_link, 'red', 'lightcoral')
        time.sleep(1)

        assert broken_link.text_content() == 'Broken Images'
        closing_element(broken_link)

        broken_link.click()
        time.sleep(1)

        #проверка картинок
        container = tab.locator('//div[@class="example"]')
        images= container.locator('img')
        count = images.count()
        print(f'Картинок в контейнере: {count}')

        broken = []

        #проверяем видимость
        for i in range(count):
            img = images.nth(i)
            image_source = img.get_attribute('src')
            is_loader = img.evaluate("""
                (img) => {
                return img.complete && img.naturalWidth > 0;
                }
            """)
            if not is_loader:
                 broken.append(image_source)
        assert len(broken) == 0, (f'\nНайдено битых картинок: {len(broken)}'
                                  f'\nСписок: {broken}')

broken_images()




