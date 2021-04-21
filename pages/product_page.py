from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    __EXPECTED_NAME__ = ''
    __EXPECTED_PRICE__ = ''

    #def should_be_product_url(self):
    #    assert "?promo=newYear" in self.browser.current_url, "There is no product page"

    def should_find_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CARD), "There is no add button on the page"
        self.__EXPECTED_NAME__ = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_EXPECTED).text
        self.__EXPECTED_PRICE__ = self.browser.find_element(*ProductPageLocators.PRICE_BEFORE_ADD_PRODUCT_TO_BASKET).text

    def should_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        button.click()

    def should_be_message_about_add(self):
        assert self.is_element_present(*ProductPageLocators.NAME_OF_ACTUAL_PRODUCT), 'there is no message about add product'

    def should_be_message_about_add_with_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRICE), 'there is no message about add product'

    def actual_name_in_the_basket(self):  # имя товара до, равно товару после
        ACTUAL_NAME_AFTER_ADD = self.browser.find_element(*ProductPageLocators.NAME_OF_ACTUAL_PRODUCT)
        assert ACTUAL_NAME_AFTER_ADD.text == self.__EXPECTED_NAME__, "we expected another name of the book"

    def actual_price_in_the_basket(self):
        ACTUAL_PRICE_AFTER_ADD = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE)
        assert ACTUAL_PRICE_AFTER_ADD.text == self.__EXPECTED_PRICE__, "we expected another price"

