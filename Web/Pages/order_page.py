

import allure

from Web.Data.data import Data
from Web.Locators.order_locators import OrderLocators
from Web.Pages.utilities import Utilities
import random


class OrderPage(Utilities, OrderLocators, Data):

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
    def click_the_product(self, locate):
        self._click(locate)

    @allure.step
    def enter_phone(self, numb):
        self._entry(self.phone_field, numb)

    @allure.step
    def enter_login_code(self, locate):
        self._entry(self.code_box, locate)

    @allure.step
    def press_login_button(self):
        self._click(self.login_button)

    @allure.step
    def press_checkout_button(self):
        self._click(self.checkout_button)

    @allure.step
    def click_plus_icon(self):
        self._click(self.add_to_cart_button)

    @allure.step
    def click_connection(self):
        self._click(self.connection_button)

    @allure.step
    def enter_name(self, locator, name):
        self._entry(locator, name)

    @allure.step
    def enter_id(self, value):
        self.my_id_num = random.randint(100000000, 1000000000)
        self._entry(value, self.my_id_num)

    @allure.step
    def enter_id_for_card(self, locate):
        self._entry(locate, self.id_card)

    @allure.step
    def enter_email(self, locate, email):
        self._entry(locate, email)

    @allure.step
    def enter_city(self, locate, address):
        self._entry(locate, address)

    @allure.step
    def enter_street(self, locate, address):
        self._entry(locate, address)

    @allure.step
    def enter_home(self, locate, address):
        self._entry(locate, address)

    @allure.step
    def enter_floor(self, locate, address):
        self._entry(locate, address)

    @allure.step
    def enter_get(self, locate, address):
        self._entry(locate, address)

    @allure.step
    def click_finish_button(self):
        self._click(self.finish)

    @allure.step
    def select_payment(self, locate):
        self._click(locate)

    @allure.step
    def enter_branch(self, locate):
        self._entry(self.branch, locate)

    @allure.step
    def enter_card_num(self, locate):
        self._entry(self.main_card, locate)

    @allure.step
    def enter_card_num_for_mobile(self, locate):
        self._entry(self.card_num, locate)

    @allure.step
    def click_confirm(self):
        self._click(self.confirm_transfer)

    @allure.step
    def click_pay(self):
        self._click(self.pay)

    @allure.step
    def back(self):
        self._click(self.back_to_home)

    @allure.step
    def click_the_field(self, locate):
        self._click(locate)

    @allure.step
    def clear_the_field(self, locator):
        self._find(locator).clear()

    @allure.step
    def _is_enabled(self, locator):
        self._wait_until_element_is_visible(locator)
        self._driver.find_element(*locator).is_enabled()

    @allure.step
    def select_exp_date(self,locate,  val,):
        self._select(locate, val)

    # def select_exp_date(self, val: str = "5", locate):
    #     self._select(locate, val)

    # @allure.step
    # def select_exp_year(self, locate, val: str = "2024"):
    #     self._select(locate, val)

    @allure.step
    def enter_credit_card(self, locate, card):
        self._entry(locate, card)

    @allure.step
    def press_credit_pay_button(self):
        self._click(self.credit_pay)

    @allure.step
    def check_on_surver(self):
        return self.retrive_data(self.phone_number2)

    @allure.step
    def switching_to_iframe(self):
        self._driver.switch_to.frame(self._find(self.iframe))


