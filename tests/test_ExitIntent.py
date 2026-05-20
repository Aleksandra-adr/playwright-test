from conftest_ui import main_tab


def test_exit_intent(main_tab):
    exit_intent_link = main_tab.locator("//a[text()='Exit Intent']")
    assert exit_intent_link.text_content() =="Exit Intent"

    exit_intent_link.click()
    main_tab.wait_for_load_state('networkidle')

    # фокус на странице, где модалка не всплывает
    string_focus = main_tab.locator("//h3[text()='Exit Intent']")
    assert string_focus.text_content() == "Exit Intent"

    string_focus.click()

    # убеждаемся что модалка не всплывает
    modal_ = main_tab.locator("div.modal")
    assert not modal_.is_visible(), "Модалка появилась при фокусе, а не должна"

    # уводим фокус
    window_size = main_tab.viewport_size
    main_tab.mouse.move(-100, -100)

    # дожидаемся появления момалки
    modal = main_tab.locator("div.modal")
    modal.wait_for(state='visible', timeout=5000)

    # нажать кнопку Закрыть внутри модалки
    close_button = main_tab.locator("//p[text()='Close']")
    assert close_button.text_content() == "Close"

    close_button.click()
    main_tab.wait_for_load_state('networkidle')

    # убеждаемся что модалка закрылась
    assert not modal.is_visible(), "Можалка отображается после закрытия"
