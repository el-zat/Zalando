from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def should_be_float_commercial(self):
        assert self.is_element_present(*MainPageLocators.FLOAT_WINDOW), "No commercial window"

    def go_to_product_page(self):
        prod_page = self.browser.find_element(*MainPageLocators.PRODUCT_TSHIRT)
        prod_page.click()


    def add_to_wishlist_button(self):
        wishlist = self.browser.find_element(*MainPageLocators.ADD_TO_WISH_LIST)
        wishlist.click()

