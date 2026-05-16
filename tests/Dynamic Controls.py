from conftest import main_tab



def test_dynamic_controls(main_tab):
    dynamic_controls_link = main_tab.locator("//a[text()='Dynamic Controls']")
    assert dynamic_controls_link.text_content() == "Dynamic Controls"

    dynamic_controls_link.click()
    main_tab.wait_for_load_state('networkidle')

    # рАБОТА С ЧЕКБОКСАМИ
    # найти активный чекбокс и отметить его
    checkbox = main_tab.locator("input[type='checkbox']")
    assert checkbox.count() == 1, "Чекбокс не найден до удаления"
    checkbox.check()

    # кликаем на кнопку remove и убеждаемся что чекбокс удален
    remove_checkbox_link = main_tab.locator("//button[text()='Remove']")
    assert remove_checkbox_link.text_content() == "Remove"

    remove_checkbox_link.click()
    main_tab.wait_for_timeout(5000)

    # убеждаемся что чекбокс удален
    assert checkbox.count() == 0, "Чекбокс все еще существует на странице!"

    message_before = main_tab.locator("//*[@id='message']")
    assert message_before.is_visible(), 'Текст "It\'s gone!" не появился'

    # кликаем на кнопку add
    add_checkbox_link = main_tab.locator("//button[text()='Add']")
    assert add_checkbox_link.text_content() == 'Add'

    add_checkbox_link.click()
    main_tab.wait_for_timeout(5000)

    # убеждаемся что чекбокс отображается
    assert checkbox.count() == 1, "Чекбокс не появился после добавления"

    message_after = main_tab.locator("//*[@id='message']")
    assert message_after.is_visible(), 'Текст "It\'s back!" не появился'

    # РАБОТА С ПОЛЕМ ВВОДА
    # убедиться что поле - дизейбл
    input_field = main_tab.locator("input[type='text']")
    assert not input_field.is_enabled(), "Поле должно быть -дизейбл, изначально"

    # нажать на enable и убедиться что поле активное
    enable_button = main_tab.locator("//button[text()='Enable']")
    enable_button.click()
    main_tab.wait_for_timeout(5000)

    assert input_field.is_enabled(), "Поле должно стать активным после нажатия на Enable"

    # вводим текст в поле
    input_field.fill("Hi, pisi and sisi")
    assert input_field.input_value() == "Hi, pisi and sisi"

    # нажать на disable и убедиться что поле неактивно
    disable_button = main_tab.locator("//button[text()='Disable']")
    disable_button.click()
    main_tab.wait_for_timeout(5000)

    assert not input_field.is_enabled(), "Поле должно быть - дизейбл, после нажатия на кнопку Disable"