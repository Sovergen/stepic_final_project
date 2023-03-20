from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def shoul_be_empty_basket_text(self):
		basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
		assert "Your basket is empty" in basket_text, "text Your basket is empty dont exist"

	def should_be_no_products_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "basket not empty"