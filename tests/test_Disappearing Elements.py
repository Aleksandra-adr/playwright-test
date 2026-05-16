from playwright.sync_api import sync_playwright


def disappearing_elements():
    with sync_playwright() as ad:
        browser = ad.chromium.launch(headless=False)
        tab = browser.new_page()
        tab.goto("https://the-internet.herokuapp.com/")
        tab.wait_for_load_state("networkidle")

        disappearing_elements_link = tab.locator("//a[contains(text(),'Disappearing')]")
        disappearing_elements_link.wait_for(state='visible', timeout=5000)
        assert disappearing_elements_link.text_content() == "Disappearing Elements"

        disappearing_elements_link.click()
        tab.wait_for_load_state("networkidle")

        # открыть каждую страницу и проверить что открывается верная ссылка
        errors = []
        buttons = tab.locator("ul li a")
        buttons.wait_for(state='visible', timeout=5000)

        for i in range(buttons.count()):
            link = buttons.nth(i) # берем конкретную ссылку
            href = link.get_attribute('href') # читаем ожидаемый URL
            text = link.text_content()
            print(f"\nПроверяю кнопку {i + 1}: '{text}' -> {href}")

            link.click()
            tab.wait_for_load_state('networkidle')

            print(f"Перешли на: {tab.url}")

            expected_url = "https://the-internet.herokuapp.com" + href
            actual_url = tab.url
            if actual_url != expected_url: # Проверяем туда ли попали
                errors.append(f"{text}: {expected_url}") # если нет , записываем ошибку

            tab.go_back() # возвращаемся на главную
            tab.wait_for_load_state('networkidle')

        assert not errors, "\n".join(errors)


disappearing_elements()




