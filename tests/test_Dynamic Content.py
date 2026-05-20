from conftest_ui import main_tab
#from playwright.sync_api import sync_playwright



def test_dynamic_content(main_tab):
    dynamic_content_link = main_tab.locator("//a[text()='Dynamic Content']")
    assert dynamic_content_link.text_content() == "Dynamic Content"

    dynamic_content_link.click()
    main_tab.wait_for_load_state('networkidle')

    # сохранить контент
    original_page_content = main_tab.locator("#content>.row").all_text_contents()

    # обновить страницу
    main_tab.reload()
    main_tab.wait_for_load_state('networkidle')

    # убедиться что контент изменился
    updated_page_content = main_tab.locator("#content>.row").all_text_contents()
    assert original_page_content != updated_page_content, "Контент не изменился"

    # нажать на click here
    click_here_button = main_tab.locator("//a[text()='click here']")
    click_here_button.click()
    main_tab.wait_for_load_state('networkidle')

    # обновить страницу
    main_tab.reload()
    main_tab.wait_for_load_state('networkidle')

    # сохранить контент
    refresh_page_content = main_tab.locator("#content>.row").all_text_contents()

    # убедиться что контент не меняется
    new_page_content = main_tab.locator('#content>.row').all_text_contents()
    assert refresh_page_content == new_page_content, "Контент изменился после клика на статический режим"



