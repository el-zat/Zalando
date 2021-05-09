from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def responses_of_product(self):
        assert self.is_element_present(*ProductPageLocators.RESPONSES), \
            "There no any responses yet"



    def another_pictures_of_product(self):
        pictures = self.browser.find_element(*ProductPageLocators.ALL_PICTURES_OF_PRODUCT_TSHIRT)
        pictures.click()

    def add_to_basket_from_product_page(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def choose_size(self):
        choose_size = self.browser.find_element(*ProductPageLocators.CHOOSE_SIZE_BUTTON)
        choose_size.click()

    def choose_xs_size(self):
        size = self.browser.find_element(*ProductPageLocators.SIZE_XS)
        size.click()

    def get_product_price_on_product_page(self):
        prod_price_on_product_page = self.browser.find_element(*ProductPageLocators.PRICE_ON_PRODUCT_PAGE)
        prod_price_on_product_page = prod_price_on_product_page.text
        prod_price_on_product_page = prod_price_on_product_page.replace(" €", "")
        prod_price_on_product_page = prod_price_on_product_page.replace(",", ".")
        return float(prod_price_on_product_page)

    def get_product_price_in_basket(self):
        prod_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        prod_price_in_basket = prod_price_in_basket.text
        prod_price_in_basket = prod_price_in_basket.replace(" €", "")
        prod_price_in_basket = prod_price_in_basket.replace(",", ".")
        return float(prod_price_in_basket)

    def choose_items_number(self):
        choose_number = self.browser.find_element(*ProductPageLocators.NUMBER_OF_ITEMS_IN_BASKET)
        choose_number.click()

    # @pytest.fixture(autouse=True)
    def choose_items(self):
        items_2 = self.browser.find_element(*ProductPageLocators.CHOOSE_2_ITEM)
        items_2.click()

    def get_number_of_items(self):
        number = self.browser.find_element(*ProductPageLocators.CHOOSE_2_ITEM)
        return int(number.text)

    def check_product_price_in_basket_and_on_product_page(self, prod_price_in_basket, prod_price_on_product_page, number):
        assert prod_price_in_basket == prod_price_on_product_page * number, \
            "Price in basket is not correct"
