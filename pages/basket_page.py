from .locators import BasketPageLocators
from .base_page import BasePage
import pytest
from .product_page import ProductPage


class BasketPage(BasePage):

    def delete_item_from_basket(self):
        delete_item = self.browser.find_element(*BasketPageLocators.DELETE_ITEM_IN_BASKET)
        delete_item.click()

    # def go_to_login_from_basket(self):
    #     login_basket =

    def go_to_payment(self):
        payment = self.browser.find_element(*BasketPageLocators.GO_TO_PAYMENT)
        payment.click()

    def remove_item_from_basket_to_wishlist(self):
        remove = self.browser.find_element(*BasketPageLocators.REMOVE_ITEM_TO_WISHLIST)
        remove.click()

    def show_pay_methods(self):
        assert self.is_element_present(*BasketPageLocators.PAYMEMT_METHODS), \
            "Payment methods are not presented"




