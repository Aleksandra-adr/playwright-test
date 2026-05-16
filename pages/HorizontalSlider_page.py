from playwright.sync_api import Page


class HorizontalSliderPage:
    SLIDER = "input[type='range']"
    VALUE = '#range'

    def __init__(self, page: Page):
        self.page = page

    def fill_slider(self, value:str):
        slider = self.page.locator(self.SLIDER)
        slider.fill(value)

    def get_value(self):
        return self.page.locator(self.VALUE).text_content()





