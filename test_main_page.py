from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_basket_is_empty_msg()




