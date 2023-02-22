import random

import allure

from Web.Data.data import Data
from Web.Locators.register_locators import RegisterLocators
from Web.Pages.utilities import Utilities


class RegisterPage(Utilities, RegisterLocators, Data):
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
    def click_myaccount_link(self):
        self._click(self.account_link)

    @allure.step
    def checking_the_title(self, locate):
        return self.text_reading(locate)

    @allure.step
    def check_the_text(self, locate):
        return self.text_reading(locate)

    @allure.step
    def enter_new_phone(self):
        self.phone = random.randint(1000000000, 10000000000)
        self._entry(self.phone_field, self.phone)
        # self.reg_phone.append(self.phone)

    @allure.step
    def enter_existing_phone(self):
        self._entry(self.phone_field, self.existing_phone)

    @allure.step
    def enter_invalid_phone(self):
        inv_phone = random.randint(10000000, 100000000)
        self._entry(self.phone_field, inv_phone)

    @allure.step
    def enter_register_code(self):
        self._entry(self.code_box, self.login_code(f'{self.phone}'))

    @allure.step
    def enter_id_number(self):
        self._entry(self.id_field, self.valid_id)

    @allure.step
    def press_perform_verification_button(self):
        self._click(self.perform_verification)

    @allure.step
    def click_checkbox(self):
        self._click(self.security_check_box)

    @allure.step
    def click_connection(self):
        self._click(self.connection_button)

    @allure.step
    def click_on_page(self):
        self._click(self.page)

    @allure.step
    def click_register_button(self):
        self._click(self.register_button)

    @allure.step
    def check_on_server(self):
        return self.retrive_data(self.phone)

    @allure.step
    def enter_name(self, locator, name):
        self._entry(locator, name)

    @allure.step
    def enter_id(self, locate, data):
        # my_id_num = random.randint(100000000, 100000000)
        self._entry(locate, data)

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
    def saving_button(self):
        self._click(self.saving)

    @allure.step
    def edit_button(self):
        self._click(self.edit)

    @allure.step
    def crate_account_button(self):
        self._click(self.crate_account)

    @allure.step
    def select_food(self):
        self._click(self.food)

    @allure.step
    def select_drink(self):
        self._click(self.drin)

    @allure.step
    def exit(self):
        self._click(self.exit_but)