def go(self, link_text: str):
    link = self.page.locator(f"//a[text()='{link_text}']")
    self.highlight(link, 'red', 'lightcoral')
    assert link.text_content() == link_text
    link.click()
    self.page.wait_for_load_state('networkidle')
    self.unhighlight(link)

def go_to( link_text, main_tab):
    link = main_tab.locator(f"//a[text()='{link_text}']")
    assert link.text_content() == link_text
    link.click()
    main_tab.wait_for_load_state('networkidle')

