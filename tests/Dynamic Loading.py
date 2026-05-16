from conftest import main_tab



def test_dynamic_loading(main_tab):
    dynamic_loading_link = main_tab.locator("//a[text()='Dynamic Loading']")
    assert dynamic_loading_link.text_content() == "Dynamic Loading"

    dynamic_loading_link.click()
    main_tab.wait_for_load_state('networkidle')

    # Найти и нажать на 1 строку
    example_1_button = main_tab.locator("//a[contains(text(),'Example 1')]")
    assert example_1_button.text_content() == "Example 1: Element on page that is hidden"

    example_1_button.click()
    main_tab.wait_for_load_state("networkidle")

    # убедиться что текст hello world не отображается до нажатия
    element = main_tab.locator("//div[@id='finish']")
    assert not element.is_visible(), " Элемент виден, а должен быть скрыт"

    # убедиться что текст есть в DOM (но не виден)
    text = element.text_content()
    assert text != "Скрытый текст", "Текст не совпадает"

    # найти и нажать кнопку Start
    start_button = main_tab.locator("//*[@id='start']")
    assert start_button.inner_text() == "Start"

    start_button.click()
    main_tab.wait_for_load_state('networkidle')

    # текст hello world отображается на странице после нажатия
    assert not element.is_visible(), "Элемент не виден, а должен быть виден"

    # вернуться на предыдущаю страницу
    main_tab.go_back()
    main_tab.wait_for_load_state('networkidle')

    # Найти и нажать на 2 строку
    example_2_button = main_tab.locator("//a[contains(text(),'Example 2')]")
    assert example_2_button.text_content() == "Example 2: Element rendered after the fact"

    example_2_button.click()
    main_tab.wait_for_load_state('networkidle')

    # убедиться что на странице и в DOM Нет текста - hello world
    element_ex2 = main_tab.locator("#finish")
    assert element_ex2.count() == 0, "Текст есть внутри DOM, Но не должен был быть"

    # найти и нажать на кнопку Start
    start_button = main_tab.locator("//*[@id='start']")
    assert start_button.inner_text() == "Start"

    start_button.click()
    main_tab.wait_for_load_state("networkidle")

    # текст hello world отображается на странице после нажатия
    assert not element.is_visible(), "Элемент не виден, а должен быть виден"
