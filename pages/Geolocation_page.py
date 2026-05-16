from playwright.sync_api import Page


class GeolocationPage:
    BUTTON = "//button" # находим любую кнопку
    LAT = '#lat-value' # локатор для элемента - ширина
    LON = '#long-value' # локатор для элемента - долгота

    def __init__(self, page: Page):
        self.page = page

    def click_button(self): # Метод для нажатия на кнопку с использованием локатора BUTTON
        self.page.locator(self.BUTTON).click() # находим кнопку и кликаем

    def get_latitude(self): # метод, возвращающий значение широты
        return self.page.locator(self.LAT).text_content() # находим элемент, берем его текст и возвращаем

    def get_longitude(self): # метод, возвращает долготу
        return self.page.locator(self.LON).text_content() #находим , берем текст и возвращаем

    # Он приостанавливает выполнение теста, пока элемент не станет видимым (или не пройдёт таймаут)
    def wait_for_coordinates(self): # метод ожидает появление элемента с широтой на странице
        self.page.wait_for_selector(self.LAT, state='visible')

