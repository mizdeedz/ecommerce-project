from pages.main_page import MainPage
from pages.wishlist_page import Wishlist

class Application():

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.wishlist_page = Wishlist(self.driver)
