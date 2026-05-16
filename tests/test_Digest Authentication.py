from playwright.sync_api import sync_playwright


def digest_authentication():
    with sync_playwright() as ad:
        browser = ad.chromium.launch(headless=False)

        # создаем контекст в учетными данными
        context = browser.new_context(
            http_credentials={
                'username': 'admin',
                'password': 'admin'
            }
        )

        tab = context.new_page()
        tab.goto("https://the-internet.herokuapp.com/")
        tab.wait_for_load_state('networkidle')

        digest_link = tab.locator('//a[contains(text(),"Digest")]')
        assert digest_link.text_content() == "Digest Authentication"

        digest_link.click()
        tab.wait_for_load_state('networkidle')

       # проверка успешной обработки
        success_text = tab.locator('//p[contains(text(), "Congratulations")]')
        assert success_text.is_visible(), "не удалось авторизоваться!"


digest_authentication()


