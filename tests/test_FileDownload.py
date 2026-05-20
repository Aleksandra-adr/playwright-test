from datetime import datetime

from playwright.sync_api import expect
from conftest_ui import main_tab



def test_file_download(main_tab):
    file_download_link = main_tab.locator("//a[text()='File Download']")
    assert file_download_link.text_content() == 'File Download'

    file_download_link.click()
    main_tab.wait_for_load_state('networkidle')

    # находим на странице все файлы
    links = main_tab.locator("//div[@class='example']/a")
    count = links.count()

    print(f"Всего ссылок: {count}")

    errors = []
    success_count = 0

    # проверяем что они кликабельны и скачиваются
    for i in range(count):
        link = links.nth(i)
        filename = link.text_content()

        if not filename or filename.strip() == '':
            continue

        # проверка - кликабельность
        try:
            if not link.is_enabled():
                errors.append(f"{filename}: не кликабелен")
                continue
        except Exception as e:
            errors.append(f"{filename}: ошибка проверка кликабельности = {e}")
            continue

        # Проверка - видимости
        try:
            if not link.is_visible():
                errors.append(f"{filename}: не виден")
                continue
        except Exception as e:
            errors.append(f'{filename}: ошибка проверки видимости - {e}')
            continue

        # Проверка - скачивание
        try:
            start_time = time.time()
            with main_tab.expect_download(timeout=10000) as download_info:
                link.click()

            download = download_info.value
            saved_name = download.suggested_filename
            elapsed = time.time() - start_time

            print(f"Скачен: {saved_name} ({elapsed:.1f}сек)")
            success_count += 1

        except Exception as e:
            errors.append(f"{filename}: ошибка скачивания - {e}")
            print(f"Ошибка скачивания - {e}")

        main_tab.wait_for_timeout(500)

    print(f"Успешно {success_count}")
    print(f"Ошибок: {len(errors)}")

    assert not errors, "\n".join(errors)




# создать отдельную функцию на проверку содержимого в файле. Нужно убедиться что содержимое соответствует всегда
# в файле - sampleFile.txt отображается дата  2025-12-24
def test_content(main_tab):
    file_download_link = main_tab.locator("//a[text()='File Download']")
    assert file_download_link.text_content() == 'File Download'

    file_download_link.click()
    main_tab.wait_for_load_state('networkidle')

    content_file = "sampleFile.txt"
    content_file_link = main_tab.locator("//a[text()='random_data.txt']")

    if content_file_link.count() == 0:
        raise AssertionError(f"Файл '{content_file} не найден на странице")

    with main_tab.expect_download() as download_info:
        content_file_link.click()

    download = download_info.value
    temp_path = download.path()

    with open(temp_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

    assert "2025-12-24" in content, f" Дата '2025-12-24' не найдена"




# в файле test-file (1).txt отображается сегодняшний месяц и год
def test_data_file(main_tab):
    file_download_link = main_tab.locator("//a[text()='File Download']")
    assert file_download_link.text_content() == 'File Download'

    file_download_link.click()
    main_tab.wait_for_load_state('networkidle')

    data_file_link = main_tab.locator("//a[text()='test-file (1).txt']")
    filename = data_file_link

    expected_date = datetime.now().strftime("%B %Y")

    with main_tab.expect_download() as download_info:
        data_file_link.click()

        download = download_info.value
        temp_path = download.path()

        with open(temp_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        assert expected_date in content, f"Дата '{expected_date}' не найдена в файле"
