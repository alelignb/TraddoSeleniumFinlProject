import allure

from Web.Pages.register_page import RegisterPage


class DdtPage(RegisterPage):

    @allure.step
    def enter_ddt_phone(self, phone):
        self._entry(self.phone_field, phone)

    @allure.step
    def enter_ddt_id(self, locate, idn):
        self._entry(locate, idn)

    @allure.step
    def enter_code_ddt(self, code):
        self._entry(self.code_box, code)

    @allure.step
    def enter_name_ddt(self, locate, name):
        self._entry(locate, name)

    @allure.step
    def enter_email_ddt(self, email):
        self._entry(self.em, email)

    @allure.step
    def enter_city_ddt(self, address):
        self._entry(self.irr,  address)

    @allure.step
    def enter_street_ddt(self, address):
        self._entry(self.mispar, address)


