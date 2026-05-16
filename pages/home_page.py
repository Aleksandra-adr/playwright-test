
from helpers.visual_helpers import color_element, closing_element

class HomePage:
    def __init__(self, page):
        self.page = page

    def go(self, link_text: str):
        link = self.page.locator(f"//a[text()='{link_text}']")
        color_element(link, 'red', 'lightcoral')
        assert link.text_content() == link_text
        link.click()
        self.page.wait_for_load_state('networkidle')


    def go_to(link_text, main_tab):
        link = main_tab.locator(f"//a[text()='{link_text}']")
        assert link.text_content() == link_text
        link.click()
        main_tab.wait_for_load_state('networkidle')

