import time
from .pages.product_page import ProductPage


def test_guest_can_choose_xs_size_and_go_to_basket_from_product_page(browser):
    link = "https://www.zalando.de/only-onlmoster-new-o-neck-t-shirt-print-jadeitecloud-dancer-on321d20v-t12.html"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(3)
    page.accept_banner()
    time.sleep(1)
    page.choose_size()
    time.sleep(1)
    page.choose_xs_size()
    time.sleep(1)
    prod_price_on_product_page = page.get_product_price_on_product_page()
    page.add_to_basket_from_product_page()
    time.sleep(1)
    page.go_to_basket()
    time.sleep(1)
    page.choose_items_number()
    page.choose_items()
    time.sleep(1)
    prod_price_in_basket = page.get_product_price_in_basket()
    number = page.get_number_of_items()
    print("Price in basket = ", prod_price_in_basket, "€")
    page.check_product_price_in_basket_and_on_product_page(prod_price_in_basket, prod_price_on_product_page, number)






