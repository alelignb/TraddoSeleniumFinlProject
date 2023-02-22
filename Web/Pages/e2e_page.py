import random

import allure

from Web.Pages.order_page import OrderPage
from Web.Pages.register_page import RegisterPage


class E2ePage(RegisterPage, OrderPage):
    my_id = random.randint(100000000, 1000000000)

    @allure.step
    def select_food(self):
        self._click(self.food)

    @allure.step
    def select_drink(self):
        self._click(self.drin)

    @allure.step
    def crate_account_button(self):
        self._click(self.crate_account)

    @allure.step
    def previous_page(self):
        self._click(self.trado)

    @allure.step
    def saving_button(self):
        self._click(self.saving)

    @allure.step
    def edit_button(self):
        self._click(self.edit)

    @allure.step
    def enter_id_num(self):
        self._entry(self.phone_field, self.my_id)

    @allure.step
    def check_on_server(self):
        return self.retrive_data(self.phone)

    @allure.step
    def enter_card_num_e2e(self, locate):
        self._entry(self.card_num, locate)

