from playwright.sync_api import Page


class FramesPage:
    NESTED_LINK = "//a[text()='Nested Frames']"
    LEFT_TEXT = "body"

    def __init__(self, page: Page):
        self.page = page

    def go_to_nested_frames(self):
        """Переходим к Nestes Frames"""
        link = self.page.locator(self.NESTED_LINK)
        link.click()
        self.page.wait_for_load_state('networkidle')

    def get_top_frame(self):
        """Возвращает верхний фрейм"""
        return self.page.frame(name='frame-top')

    def get_bottom_frame(self):
        """Возвращаем нижний фрейм"""
        return self.page.frame(name='frame-bottom')

    def get_left_frame(self):
        """Возвращаем левый фрейм"""
        return self.page.frame(name='frame-left')

    def get_middle_frame(self):
        """Возвращаем средний фрейм"""
        return self.page.frame(name='frame-middle')

    def get_right_frame(self):
        """Возвращаем правый фрейм"""
        return self.page.frame(name='frame-right')

    def get_frame_text(self, frame):
        """Возвращаем текствнутри фреймов"""
        if frame:
            return frame.locator(self.LEFT_TEXT).text_content().strip()
        return None
