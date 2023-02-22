import time

import allure

from Web.Data.data import Data
from Web.Locators.login_locators import LoginLocators
from Web.Pages.utilities import Utilities


class LoginPage(Utilities, LoginLocators, Data):
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
        time.sleep(3)

    @allure.step
    def checking_the_title(self, locate):
        return self.text_reading(locate)

    @allure.step
    def check_the_text(self, locate):
        return self.text_reading(locate)

    @allure.step
    def click_the_link(self, locate):
        self._click(locate)

    @allure.step
    def enter_phone(self):
        self._entry(self.phone_field, self.new_phone)

    @allure.step
    def enter_invalid_phone(self):
        self._entry(self.phone_field, self.invalid_phone2)

    @allure.step
    def enter_login_code(self):
        self._entry(self.code_box, self.login_code(f'{self.new_phone}'))

    @allure.step
    def press_login_button(self):
        self._click(self.login_button)
        time.sleep(2)

    @allure.step
    def click_checkbox(self, locate):
        self._click(locate)

    @allure.step
    def click_connection(self):
        self._click(self.connection_button)

    @allure.step
    def etrado_page_title(self):
        self.text_reading(self.etrado_title)

    @allure.step
    def click_on_page(self):
        self._click(self.page)
