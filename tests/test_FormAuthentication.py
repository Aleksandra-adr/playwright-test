from pyexpat.errors import messages

from conftest import main_tab


def test_form_authentication_positive(main_tab):
    login_page_link = main_tab.locator("//a[text()='Form Authentication']")
    assert login_page_link.text_content() == "Form Authentication"

    login_page_link.click()
    main_tab.wait_for_load_state('networkidle')

    # ПОЗИТИВНЫЙ
    # найти поле Username
    username = main_tab.locator("label[for=username]")
    assert username.count() > 0, "Поле ввода имени не найдено"

    # убедиться что оно кликабельно и ввести "tomsmith"
    assert username.is_visible(), "Поле ввода имени неактивно"
    username.fill("tomsmith")

    # найти поле password
    password = main_tab.locator("label[for=password]")
    assert password.count() > 0, "Поле ввода пароля не найдено"

    # убедиться что оно кликабельное и ввести "SuperSecretPassword!"
    assert password.is_visible(), "Поле ввода пароля не кликабельно"
    password.fill("SuperSecretPassword!")

    # найти кнопку Login и нажать на нее
    login_page = main_tab.locator("button")
    assert login_page.count() > 0, "Кнопка отправки не найдена"

    assert login_page.is_visible(), "Кнопка отправки не кликабельна"
    login_page.click()
    main_tab.wait_for_load_state('networkidle')

    # убеждаемся об успехе
    assert "/secure" in main_tab.url, "URL не изменился"

    message = main_tab.locator("div[id=flash]")
    assert message.is_visible(), "Сообщение об успехе не появилось"


def test_form_authentication_negative1(main_tab):
    login_page_link = main_tab.locator("//a[text()='Form Authentication']")
    assert login_page_link.text_content() == "Form Authentication"

    login_page_link.click()
    main_tab.wait_for_load_state('networkidle')

    # НЕГАТИВНЫЙ
    # находим кнопку и нажимаем
    login_page = main_tab.locator("button")
    assert login_page.count() > 0, "Кнопка отправить не найдена"

    assert login_page.is_visible(), "Кнопка отправить не кликабельна"
    login_page.click()
    main_tab.wait_for_load_state('networkidle')

    # убеждаемся об ошибке
    assert "/login" in main_tab.url, "URL не изменился"

    message = main_tab.locator("div[id=flash]")
    assert message.is_visible(), "Сообщение об ошибке не появилось"
