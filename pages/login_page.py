from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "Url doesn't contain substring 'login' "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not present"

    def register_new_user(self, email, password):
        self.fill_out_input_field(*LoginPageLocators.REGISTRATION_EMAIL_INPUT, email)
        self.fill_out_input_field(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT, password)
        self.fill_out_input_field(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_INPUT, password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
