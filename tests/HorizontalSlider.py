from Welcome.conftest import main_tab
from Welcome.pages.HorizontalSlider_page import HorizontalSliderPage
from Welcome.pages.home_page import go_to



def test_slider_fill(main_tab):
    go_to('Horizontal Slider', main_tab)

    slider = HorizontalSliderPage(main_tab)
    slider.fill_slider("4")
    assert slider.get_value() == '4'

    # # найти слайдер
    # slider = main_tab.locator("input[type='range']")
    #
    # # используем fill
    # slider.fill('4')
    #
    # value = main_tab.locator('#range')
    # assert value.text_content() == '4'


def test_slider_arrow(main_tab):
    go_to('Horizontal Slider', main_tab)

    slider = HorizontalSliderPage(main_tab)
    slider.page.locator(slider.SLIDER).click()

    for i in range(20):
        main_tab.keyboard.press('ArrowLeft')

    for i in range(4):
     main_tab.keyboard.press('ArrowRight')

    assert float(slider.get_value()) == 2


    # # найти слайдер
    # slider = main_tab.locator("input[type='range']")
    # slider.click()
    #
    # # уводим слайдер в самый левый край из-за шагов выше
    # for i in range(20):
    #     main_tab.keyboard.press('ArrowLeft')
    #
    # # после того как значение точно стало 0, делаем шаги с помощью клавиатуры
    # for i in range(4):
    #     main_tab.keyboard.press('ArrowRight')
    #
    # assert float(main_tab.locator('#range').text_content()) == 2


