from conftest import main_tab



def test_forgot_password(main_tab):
    forgot_link = main_tab.locator("//a[text()='Forgot Password']")
    assert  forgot_link.text_content() == "Forgot Password"

    forgot_link.click()
    main_tab.wait_for_load_state('networkidle')

    # найти поле ввода
    input_mail = main_tab.locator("input")
    assert input_mail.count() > 0, "Поле ввода не найдено"

    assert input_mail.is_visible(), " Поле ввода не активно"
    input_mail.fill("test@example.com")

    # найти кнопку
    button = main_tab.locator("button[type=submit]")
    assert button.count() > 0, " Кнопка не найдена"

    assert button.is_enabled(), "Кнопка не кликабельна"
    button.click()
    main_tab.wait_for_load_state('networkidle')

    # убедиться что пароль успешно отправлен
    assert "/email_sent" in main_tab.url, "URL не изменился"

