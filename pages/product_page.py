from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_product_to_basket(self):
		add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		add_to_basket_button.click()

	def should_be_add_rigt_product(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ELEMENT).text
		added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
		assert product_name == added_product_name, f"expected added product name :'{product_name}', but real:'{added_product_name}'"

	def should_be_right_basket_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ELEMENT).text
		added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
		assert product_price == added_product_price, f"expected added product price :'{product_price}', but real:'{added_product_price}'"

	def should_not_be_success_message_present(self):
		assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "success message is showed"

	def should_be_desapired_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME), f"success message is not desapiered"
