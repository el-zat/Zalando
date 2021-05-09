from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def accept_banner(self):
        accept_banner = self.browser.find_element(*BasePageLocators.ACCEPT_BANNER)
        accept_banner.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_go_to_product_category(self):
        self.go_to_product_category_women()
        self.go_to_product_category_men()
        self.go_to_product_category_kids()

    def should_go_to_product_type(self):
        self.go_to_product_type_clothes()
        self.go_to_product_type_shoes()
        self.go_to_product_type_sport()
        self.go_to_product_type_accessories()

    def go_to_basket(self):
        basket = self.browser.find_element(*BasePageLocators. BASKET_BUTTON)
        basket.click()

    def go_to_wishlist(self):
        wishlist = self.browser.find_element(*BasePageLocators.WISHLIST_BUTTON)
        wishlist.click()

    def go_to_homepage(self):
        homepage = self.browser.find_element(*BasePageLocators.HOME_BUTTON)
        homepage.click()

    def number_items_in_basket(self):
        assert self.is_element_present(*BasePageLocators.NUMBER_ITEMS_IN_BASKET), \
            "Number of items in basket ist not presented"

    def number_items_in_wishlist(self):
        assert self.browser.is_element_present(*BasePageLocators.NUMBER_ITEMS_IN_WISHLIST), \
            "Number of items in wishlist ist not presented"

    def go_to_product_category_women(self):
        prod_cat_women = self.browser.find_element(*BasePageLocators.CAT_WOMEN)
        prod_cat_women.click()

    def go_to_product_category_men(self):
        prod_cat_men = self.browser.find_element(*BasePageLocators.CAT_MEN)
        prod_cat_men.click()

    def go_to_product_category_kids(self):
        prod_cat_kids = self.browser.find_element(*BasePageLocators.CAT_KIDS)
        prod_cat_kids.click()

    def go_to_product_type_clothes(self):
        prod_cat_clothes = self.browser.find_element(*BasePageLocators.PROD_TYPE_CLOTHES)
        prod_cat_clothes.click()

    def go_to_product_type_shoes(self):
        prod_cat_shoes = self.browser.find_element(*BasePageLocators.PROD_TYPE_SHOES)
        prod_cat_shoes.click()

    def go_to_product_type_sport(self):
        prod_cat_sport = self.browser.find_element(*BasePageLocators.PROD_TYPE_SPORT)
        prod_cat_sport.click()

    def go_to_product_type_accessories(self):
        prod_cat_accessories = self.browser.find_element(*BasePageLocators.PROD_TYPE_ACCESSOIRES)
        prod_cat_accessories.click()

    def go_to_login_page(self):
        login_page = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        login_page.click()