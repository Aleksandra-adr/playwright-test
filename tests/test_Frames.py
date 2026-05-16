from Welcome.conftest import main_tab
from Welcome.pages.Frames_page import FramesPage
from Welcome.pages.home_page import go_to


def test_frames_nested_frames(main_tab):
    go_to('Frames', main_tab)

    frames = FramesPage(main_tab)
    frames.go_to_nested_frames()

    # получаем фреймы
    top = frames.get_top_frame()
    assert top is not None, 'Фрейм "frame-top" не найден'

    bottom = frames.get_bottom_frame()
    assert bottom is not None, 'Фрейм "frame-bottom" не найден'

    left = frames.get_left_frame()
    assert left is not None, 'Фрейм "frame-left" не найден'

    middle = frames.get_middle_frame()
    assert middle is not None, 'Фрейм "frame-middle" не найден'

    right = frames.get_right_frame()
    assert right is not None, 'Фрейм "frame-right" не найден'

    # проверка текстов
    assert frames.get_frame_text(left) == "LEFT"
    assert frames.get_frame_text(middle) == 'MIDDLE'
    assert frames.get_frame_text(right) == 'RIGHT'
    assert frames.get_frame_text(bottom) == 'BOTTOM'

    # frames_link = main_tab.locator("//a[text()='Frames']")
    # assert  frames_link.text_content() == "Frames"
    #
    # frames_link.click()
    # main_tab.wait_for_load_state("networkidle")

    # Nested Frames
    # найти строку Nested Frames и провалиться
    # nested_link = main_tab.locator("//a[text()='Nested Frames']")
    # assert nested_link.text_content() == "Nested Frames"
    #
    # nested_link.click()
    # main_tab.wait_for_load_state('networkidle')

    # получаем все фреймы
    # top_frame = main_tab.frame(name='frame-top')
    # assert top_frame is not None, 'Фрейм "frame-top" не найден'

    # bottom_frame = main_tab.frame(name='frame-bottom')
    # assert bottom_frame is not None, 'Фрейм "frame-bottom" не найден'

    # left_frame = main_tab.frame(name='frame-left')
    # assert left_frame is not None, 'Фрейм "frame-left" не найден'

    # middle_frame = main_tab.frame(name='frame-middle')
    # assert middle_frame is not None, 'Фрейм "frame-middle" не найден'

    # right_frame = main_tab.frame(name='frame-right')
    # assert right_frame is not None, 'Фрайм "frame-right" не найден'

    # проверка содержимого
    # left_text = left_frame.locator("body").text_content().strip()
    # assert left_text == 'LEFT', f"Ожидали 'LEFT', получили {left_text}"
    #
    # middle_text = middle_frame.locator('body').text_content().strip()
    # assert middle_text == "MIDDLE", f"Ожидали 'MIDDLE', получили {middle_text}"
    #
    # right_text = right_frame.locator('body').text_content().strip()
    # assert right_text == "RIGHT", f'Ожидали "RIGHT", получили {right_text}'
    #
    # bottom_text = bottom_frame.locator('body').text_content().strip()
    # assert bottom_text == "BOTTOM", f'Ожидали "BOTTOM", получили {bottom_text}'


def test_frames_iframe(main_tab):
    frames_link = main_tab.locator("//a[text()='Frames']")
    assert frames_link.text_content() == "Frames"

    frames_link.click()
    main_tab.wait_for_load_state("networkidle")

    # iFrame
    # найти строку и провалиться
    nested_link = main_tab.locator("//a[text()='iFrame']")
    assert nested_link.text_content() == "iFrame"

    nested_link.click()
    main_tab.wait_for_load_state('networkidle')

    # Закрытие алерта
    close_alert = main_tab.locator("//div[@class='tox-icon']")
    close_alert.click()


