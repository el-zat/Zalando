import time
from .pages.login_page import LoginPage


def test_guest_can_login_with_email_and_password_from_main_page_and_go_to_basket(browser):
    link = "https://www.zalando.de/login?target=/myaccount/"
    page = LoginPage(browser, link)
    page.open()
    time.sleep(3)
    page.accept_banner()
    time.sleep(1)
    page.put_email()
    page.put_password()
    time.sleep(3)
    page.press_login_button()
    time.sleep(5)