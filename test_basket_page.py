from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time


# def test_guest_can_delete_items_from_basket(browser):
#     link1 = "https://www.zalando.de/only-onlmoster-new-o-neck-t-shirt-print-jadeitecloud-dancer-on321d20v-t12.html"
#     page = ProductPage(browser, link1)
#     page.open()
#     time.sleep(3)
#     page.accept_banner()
#     time.sleep(1)
#     page.choose_size()
#     time.sleep(1)
#     page.choose_xs_size()
#     time.sleep(1)
#     page.add_to_basket_from_product_page()
#     link2 = 'https://www.zalando.de/cart'
#     page = BasketPage(browser, link2)
#     page.open()
#     time.sleep(3)
#     page.delete_item_from_basket()
#     time.sleep(3)


def test_guest_can_go_to_payment_from_basket_and_choose_payment(browser):
    link1 = "https://www.zalando.de/login?target=/myaccount/"
    page = LoginPage(browser, link1)
    page.open()
    time.sleep(3)
    page.accept_banner()
    time.sleep(1)
    page.put_email()
    page.put_password()
    time.sleep(3)
    page.press_login_button()
    time.sleep(5)
    link2 = "https://www.zalando.de/only-onlmoster-new-o-neck-t-shirt-print-jadeitecloud-dancer-on321d20v-t12.html"
    page = ProductPage(browser, link2)
    page.open()
    time.sleep(3)
    page.choose_size()
    time.sleep(1)
    page.choose_xs_size()
    time.sleep(1)
    page.add_to_basket_from_product_page()
    time.sleep(1)
    page.go_to_basket()
    time.sleep(3)
    link3 = 'https://www.zalando.de/cart'
    page = BasketPage(browser, link3)
    page.open()
    time.sleep(3)
    page.go_to_payment()
    time.sleep(3)
