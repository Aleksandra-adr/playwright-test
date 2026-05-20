import time

from selenium.webdriver.common.devtools.v136.fetch import continue_request

from conftest_ui import main_tab


def test_floating_menu_simple(main_tab):
    floating_link = main_tab.locator("//a[text()='Floating Menu']")
    floating_link.click()
    main_tab.wait_for_load_state('networkidle')

    buttons = main_tab.locator("#menu a")

    for i in range(buttons.count()):
        btn = buttons.nth(i)
        text = btn.text_content()
        href = btn.get_attribute('href')

        print(f"\nКнопка: {text} (href='{href}')")

        # Проверяем, что кнопка кликабельна
        assert btn.is_enabled(), f"{text}: не кликабельна"
        assert btn.is_visible(), f"{text}: не видима"

        # Кликаем
        btn.click()
        time.sleep(0.5)

        # Проверяем, что URL содержит якорь
        assert href in main_tab.url, f"Якорь '{href}' не добавлен в URL"

        print(f"Клик успешен, URL: {main_tab.url}")

    print("\nВсе кнопки Floating Menu работают корректно!")



