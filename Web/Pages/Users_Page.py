import allure

from Web.Data.data import Data
from Web.Locators.Locators_users import Locators_user
from Web.Pages.utilities import Utilities


class UsersPage(Utilities, Locators_user, Data):

    @allure.step
    @allure.description("Insert phone number")
    def insert_login_phone_no(self):
        self._entry(self.login_phone_field,self.phone_admin)

    @allure.step
    @allure.description("click on send me code button")
    def send_me_code_button(self):
        self._click(self.send_me_code_btn)

    @allure.step
    @allure.description("Insert add user data on fild")
    def insert_datas(self, locate, fild_data):
        self._entry(locate, fild_data)

    @allure.step
    @allure.description("Insert password number")
    def insert_login_password(self):
        self._entry(self.login_password_field, self.password_admin)

    @allure.step
    @allure.description("click on login button")
    def login_button(self):
        self._click(self.login_btn)


    @allure.step
    @allure.description("click on users category")
    def click_users_category(self):
        self._click(self.users)
        text = self._find(self.users_text).text
        assert text in "משתמשים"

    @allure.step
    @allure.description("click on users maximize button")
    def click_users_maximize_btn(self):
        self._click(self.users_btn)

    @allure.step
    @allure.description("click on users setting button")
    def click_users_settings(self):
        self._click(self.setting)

    @allure.step
    @allure.description("search user on the search bar")
    def search_users(self, data):
        self._entry(self.search, data)

    @allure.step
    @allure.description("click on add users button")
    def click_on_add_users(self):
        self._click(self.add_user)
        text = self._find(self.add_user_text).text
        assert text in "משתמשים"

    @allure.step
    @allure.description("click on add users x button")
    def click_add_users_x_btn(self):
        self._click(self.add_user_x_btn)

    @allure.step
    @allure.description("switch on active button ")
    def switch_on_active_btn(self):
        self._click(self.active_btn)

    @allure.step
    @allure.description("click on add users button")
    def click_add_users_btn(self):
        self._click(self.add_user_btn)

    @allure.step
    @allure.description("switch on ETrado approved")
    def switch_on_etrado_approved(self):
        self._click(self.ETrado_approved)

    @allure.step
    @allure.description("click on update button")
    def click_on_update_btn(self):
        self._click(self.update_btn)

    @allure.step
    @allure.description("click on numbers display button")
    def click_on_number_display_btn(self):
        self._click(self.numbers_display_button)

    @allure.step
    @allure.description("click on numbers display potions")
    def click_on_number_display_options(self, option):
        self._click(option)

    @allure.step
    @allure.description("click on user setting categories")
    def click_on_user_setting_categories(self, option):
        self._click(option)

    @allure.step
    @allure.description("click on the arrows")
    def click_on_arrows(self, option):
        self._click(option)

    @allure.step
    @allure.description("click on the change language icons")
    def click_language_icons(self, option):
        self._click(option)






















