from .pages.product_page import ProductPage
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_busket()
    page.should_match_product_name()
    page.should_match_product_price()

