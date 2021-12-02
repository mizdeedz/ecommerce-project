from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):
    TOP_BANNER = (By.CSS_SELECTOR, 'div.slider.slider-nav-large')
    RIGHT_ARROW = (By.CSS_SELECTOR, 'button[aria-label="Next"] svg.flickity-button-icon')
    LEFT_ARROW = (By.CSS_SELECTOR, 'button[aria-label="Previous"] svg.flickity-button-icon')
    RIGHT_DOT = (By.CSS_SELECTOR, 'li[aria-label="Page dot 2"]')
    LEFT_DOT = (By.CSS_SELECTOR, 'li[aria-label="Page dot 1"]')
    NEXT_PRODUCT_NAME = (By.XPATH, '//div[@class="text-inner text-center"]//strong[contains(text(), "Mac")]')
    FIRST_PRODUCT_NAME = (By.XPATH, '//div[@class="text-inner text-left"]//strong[contains(text(), "iPad")]')
    NEXT_PRODUCT = ''
    FIRST_PRODUCT = ''
    FIRST_PRODUCT_TEXT = ''

    def open_main_page(self):
        self.open_page()

    def hover_over_top_banner(self):
        banner = self.find_element(*self.TOP_BANNER)
        actions = ActionChains(self.driver)
        actions.move_to_element(banner)
        actions.perform()

    def click_right_arrow(self):
        self.wait_for_element_click(*self.RIGHT_ARROW)
        sleep(2)

    def click_left_arrow(self):
        self.wait_for_element_click(*self.LEFT_ARROW)
        sleep(2)

    def click_bottom_right_dot(self):
        self.wait_for_element_click(*self.RIGHT_DOT)
        sleep(2)

    def click_bottom_left_dot(self):
        self.wait_for_element_click(*self.LEFT_DOT)
        sleep(2)

    def store_next_product_name(self):
        self.NEXT_PRODUCT = self.find_element(*self.NEXT_PRODUCT_NAME).text
        print(f'Next Product Name is {self.NEXT_PRODUCT}')

    def store_first_product_name(self):
        self.FIRST_PRODUCT = self.find_element(*self.FIRST_PRODUCT_NAME).text
        self.FIRST_PRODUCT_TEXT = self.FIRST_PRODUCT[1::]
        print(f'First Product Name is {self.FIRST_PRODUCT_TEXT}')

    def verify_product_text(self):
        assert self.FIRST_PRODUCT_TEXT != self.NEXT_PRODUCT, f'Error! Actual {self.FIRST_PRODUCT_TEXT} ' \
                                                      f'does not differ from Expected {self.NEXT_PRODUCT}'

    def verify_banner_link_clicks(self):
        sleep(1)
