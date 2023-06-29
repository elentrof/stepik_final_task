from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage):
    def add_product_to_busket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()
        self.solve_quiz_and_get_code()

    def should_match_product_name(self):
        our_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME).text
        assert our_product == product_in_basket_name, "Product name doesn't match"

    def should_match_product_price(self):
        our_product_price = self.our_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_in_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE).text
        assert our_product_price == product_in_basket_price, "Product price doesn't match"

    # проверка, что нет сообщения о добавлении в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"











