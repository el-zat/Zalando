from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):

    def put_email(self):
        email = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email.send_keys("mariazat@yahoo.com")

    def put_password(self):
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password.send_keys("Polar3311")

    def press_login_button(self):
        login = self.browser.find_element(*LoginPageLocators.LOGIN)
        login.click()

