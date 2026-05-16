import time

from conftest import main_tab


def test_file_upload(main_tab):
    file_upload_link = main_tab.locator("//a[text()='File Upload']")
    assert file_upload_link.text_content() == "File Upload"

    file_upload_link.click()
    main_tab.wait_for_load_state('networkidle')

    # выбрать файл и загрузить
    file_input = main_tab.locator("#file-upload")
    file_input.set_input_files("C:/Users/Professional/Desktop/тест.txt")

    main_tab.locator("#file-submit").click()

    success_message = main_tab.locator("h3")
    assert 'File Uploaded!' in success_message.text_content()


