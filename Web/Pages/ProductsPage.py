import allure

from Web.Data.data2 import Data2
from Web.Locators.ProductsLocators import AdminProductsLocators
from Web.Pages.utilities import Utilities


class ProductPage(Utilities, AdminProductsLocators, Data2):

    @allure.step
    def verify_the_title_of_the_page(self, page):
        return self._find(page).text

    @allure.step
    def displaying(self, display):
        return self._is_displayed(display)

    @allure.step
    def verifying_success_message(self, success_message):
        return self._find(success_message).text

    @allure.step
    def fill_phone_code(self, phone):
        self._entry(self.phone_code, phone)

    @allure.step
    def click_on_submit(self):
        self._click(self.form_submit_button)

    @allure.step
    def fill_admin_code(self, code_admin):
        self._entry(self.phone_code, code_admin)

    @allure.step
    def fill_bar_code(self, bar_codes):
        self._entry(self.bar_code, bar_codes)

    @allure.step
    def fill_product_name(self, product):
        self._entry(self.product_name, product)

    @allure.step
    def fill_price(self, prices):
        self._entry(self.price, prices)

    @allure.step
    def fill_date(self, dates):
        self._entry(self.date, dates)

    @allure.step
    def fill_description(self, descriptions):
        self._entry(self.description, descriptions)

    @allure.step
    def remember_click_on(self):
        self._click(self.remember_click)

    @allure.step
    def click_on_next(self):
        self._click(self.next_button)

    @allure.step
    def click_on_login(self):
        self._click(self.form_login)

    @allure.step
    def click_on_products(self, click):
        self._click(click)

    @allure.step
    def click_on_product1(self, click):
        self._click(click)

    @allure.step
    def selection_click(self, sectionId):
        self._click(sectionId)

    @allure.step
    def selection_send(self, section_id, content):
        self._entry(section_id, content)

    @allure.step
    def click_on_selection(self, selection):
        self._click(selection)

    @allure.step
    def click_on_add(self, add):
        self._click(add)

    @allure.step
    def indication_alert(self, indication):
        return self._find(indication).text

    @allure.step
    def color(self, location):
        element_color = self._find(location).value_of_css_property("background-color")
        return element_color

    @allure.step
    def checking_font_size(self, location):
        return self._find(location).value_of_css_property("font-size")

    @allure.step
    def checking_font_weight(self, location):
        return self._find(location).value_of_css_property("font-weight")

    @allure.step
    def checking_text_align(self, location):
        return self._find(location).value_of_css_property("text-align")
