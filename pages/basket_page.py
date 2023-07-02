from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    # проверка, что нет сообщения о добавлении в корзину
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BUSKET), \
            "Products are presented, but should not be"
        print('products empty OK')

    def should_basket_is_empty_msg(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MSG), "'Basket is empty' message is not presented"
        print('message empty OK')