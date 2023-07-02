from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    # MESSAGES_FORM = (By.CSS_SELECTOR, '#messages .alert-safe .alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    PRODUCT_IN_BASKET_NAME = (By.CSS_SELECTOR, '#messages > .alert.alert-success:nth-child(1) > .alertinner strong')
    PRODUCT_IN_BASKET_PRICE = (By.CSS_SELECTOR, '#messages > .alert.alert-info > .alertinner strong')



