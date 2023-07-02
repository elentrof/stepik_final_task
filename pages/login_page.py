from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f"expected 'login' to be substring of '{self.browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Rigester form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FOR_REGISTRATION), "there is no login field in registration form"
        assert self.is_element_present(*LoginPageLocators.PWD_FOR_REGISTRATION), "there is no password field in registration form"
        assert self.is_element_present(*LoginPageLocators.PWD_REPEAT_REGISTRATION), "there is no password-repeat field in registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "there is no submit button in registration form"

        login = self.browser.find_element(*LoginPageLocators.LOGIN_FOR_REGISTRATION)
        login.send_keys(email)

        pwd = self.browser.find_element(*LoginPageLocators.PWD_FOR_REGISTRATION)
        pwd.send_keys(email)

        pwd_repeat = self.browser.find_element(*LoginPageLocators.PWD_REPEAT_REGISTRATION)
        pwd_repeat.send_keys(email)

        sbmt = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        sbmt.click()

