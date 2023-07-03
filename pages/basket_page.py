from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        """
        проверка, что нет сообщения о добавлении в корзину
        """
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BUSKET), \
            "Products are presented, but should not be"
        print('products empty OK')

    def should_basket_is_empty_msg(self):
        """
        проверка, что есть сообщение о том, что корзина пуста
        """
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MSG), "'Basket is empty' message is not presented"
        print('message empty OK')