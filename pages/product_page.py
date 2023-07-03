from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage):
    def add_product_to_busket(self):
        """
        добавление  продукта в корзину на страницах, где есть задача(промо)
        """
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()
        self.solve_quiz_and_get_code()

    def add_product_to_busket_without_quiz(self):
        """
        добавление продукта в корзину на страницах, где нет решения задачи(без промо)
        """
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()

    def should_match_product_name(self):
        """
        проверка, что имя товара совпадает с наименованием в блоке о добавлении в корзину
        """
        our_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME).text
        assert our_product == product_in_basket_name, "Product name doesn't match"

    def should_match_product_price(self):
        """
        проверка, что цена товара совпадает в ценой в блоке добавления в корзину
        """
        our_product_price = self.our_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_in_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE).text
        assert our_product_price == product_in_basket_price, "Product price doesn't match"

    def should_not_be_success_message(self):
        """
        проверка, что нет сообщения о добавлении в корзину
        """
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_NAME), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        """
        проверка, что сообщение о добавлениии в корзину исчезает
        """
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_BASKET_NAME), \
            "Success message is presented, but should not be"
















