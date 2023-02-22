import time

import allure
from selenium.webdriver.common.by import By

from Web.Data.data import Data
from Web.Locators.cart_locators import CartLocators
from Web.Pages.utilities import Utilities


class CartPage(Utilities, CartLocators, Data):

    @allure.step
    def select_option1(self):
        self._click(self.option1)

    @allure.step
    def select_option2(self):
        self._click(self.option2)

    @allure.step
    def click_save_button(self):
        self._click(self.save)

    @allure.step
    def check_the_title_of_cart_is_correct(self):
       return self.text_reading(self.cart_title)

    @allure.step
    def check_the_cart_is_empty_without_adding_products(self):
        return self.text_reading(self.empty_cart)

    @allure.step
    def check_total_price_on_cart(self, locate):
        return float(self.extracted_num(locate))

    @allure.step
    def total_price_calculation(self, locate):
        return self.total_price_calc(locate)

    @allure.step
    def click_the_product(self, locate):
        self._click(locate)

    @allure.step
    def adding_to_cart(self):
        self._click(self.add_to_cart_button)
        time.sleep(1)

    @allure.step
    def click_the_button(self, locate):
        self._click(locate)
        time.sleep(1)

    @allure.step
    def switching_frame(self):
        self._driver._switch_to(self.cart_frame)

    @allure.step
    def double_click_on_addition(self, locate):
        for i in range(2):
            self._click(locate)
            time.sleep(2)

    @allure.step
    def amout_on_cart(self):
        num = int(self._find(self.product_counter).get_attribute("value"))
        return num

    @allure.step
    def add_products(self):
        products = self._find_elements(self.products_path)
        return len(products)

    @allure.step
    def checking_subtotal_and_bolded_prices(self):
        comp_prices = []
        for i in range(self.add_products()):
            location = (By.XPATH, f'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[3]/a[{i + 1}]/div[1]/div[2]/div[2]/div[1]')
            self._click(location)
            self._click(self.add_to_cart_button)
            price1 = self.extracted_num(self.bolded_price)
            price2 = self.extracted_num(self.pr_price_after_add)
            if price1 != price2:
                comp_prices.append(False)
            self._click(self.delete)
            self._driver.back()
        return len(comp_prices)

    @allure.step
    def check_product_price(self, locate):
        self.extracted_num(locate)

    @allure.step
    def checking_products_are_displayed_on_cart(self):
        for i in range(4):
            location = (By.XPATH, f'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[3]/a[{i + 1}]/div[1]/div[2]/div[2]/div[1]')
            self._click(location)
            self._click(self.add_to_cart_button)
            self._driver.back()
        products = self._find_elements(self.products_on_cart)
        if len(products) == 4:
            return True









