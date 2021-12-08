from selenium.webdriver.common.by import By
from pages.base_page import Page

class Wishlist(Page):
    EMPTY_WISHLIST_TEXT = (By.CSS_SELECTOR, 'td.wishlist-empty')

    def open_gettop_wishlist(self):
        self.open_page('my-account/wishlist/')

    def verify_expected_text_displays(self, expected_text):
        self.verify_text(expected_text, *self.EMPTY_WISHLIST_TEXT)
