from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME_ELEMENT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ELEMENT = (By.CSS_SELECTOR, ".product_main p")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) div p strong")

