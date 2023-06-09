import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self,browser):
		link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		register_page = LoginPage(browser, link)
		register_page.open()
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time())
		register_page.register_new_user(email=email , password=password)
		register_page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_not_be_success_message_present()

	#I am cut parameters quantity for esieer check
	@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
	                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
	                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"])
	def test_user_can_add_product_to_basket(self, browser, link):
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.add_product_to_basket()
		product_page.solve_quiz_and_get_code()
		product_page.should_be_add_rigt_product()
		product_page.should_be_right_basket_price()

@pytest.mark.need_review
def test_guest_cant_see_success_message(browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_not_be_success_message_present()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.got_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_no_products_in_basket()
	basket_page.shoul_be_empty_basket_text()



@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_product_to_basket()
	product_page.should_not_be_success_message_present()
 
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_product_to_basket()
	product_page.should_be_sesapired_success_message()
