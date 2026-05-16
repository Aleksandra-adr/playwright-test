import time

from conftest import main_tab



def test_entry_ad(main_tab):
    entry_ad_link = main_tab.locator("//a[text()='Entry Ad']")
    assert entry_ad_link.text_content() == "Entry Ad"

    entry_ad_link.click()
    main_tab.wait_for_load_state('networkidle')

    # ждем появления модалки
    modal = main_tab.locator("//div[@class='modal']")
    modal.wait_for(state='visible', timeout=5000)

    # в открывшейся модалке нажать на кнопку Close
    close_button = main_tab.locator("//p[text()='Close']")
    assert close_button.text_content() == "Close"

    close_button.click()
    time.sleep(3)
    modal.wait_for(state='hidden', timeout=8000)

    # обновить страницу
    main_tab.reload()
    main_tab.wait_for_load_state('networkidle')

    # убедиться что модалка не открылась
    modal_after = main_tab.locator("//div[@class='modal']")
    assert modal_after.count() == 0 or not modal_after.is_visible(), " Модалка появилась при обновлении"
