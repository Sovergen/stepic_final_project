from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK          = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID  = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_BUTTON       = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON           = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS        = (By.CSS_SELECTOR, "form#basket_formset div.basket-items")
    EMPTY_BASKET_TEXT   = (By.CSS_SELECTOR, ".content div#content_inner p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM                  = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM               = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT    = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON         = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON    = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME_ELEMENT    = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ELEMENT   = (By.CSS_SELECTOR, ".product_main p")
    ADDED_PRODUCT_NAME      = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    ADDED_PRODUCT_PRICE     = (By.CSS_SELECTOR, "#messages div:nth-child(3) div p strong")

