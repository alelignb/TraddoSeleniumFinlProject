
import allure
from Web.Data.data4 import Data4
from Web.Locators.dashboard_locators import Dashboard_Locators
from Web.Pages.utilities import Utilities


class dashboard_page(Utilities, Dashboard_Locators, Data4):

    @allure.step
    def fill_values_to_phone_correct(self, correct_phone_number):
        self._entry(self.correct_phone_number, correct_phone_number)

    @allure.step
    def click_on_phone_code(self):
        self._click(self.phone_code)

    @allure.step
    def fill_values_to_passward_field(self, valid_passward):
        self._entry(self.correct_passward, valid_passward)

    @allure.step
    def click_on_check_box(self):
        self._click(self.check_box)

    @allure.step
    def click_on_connection_button(self):
        self._click(self.connection_button)

    @allure.step
    def click_on_dsheboard_button(self):
        self._click(self.dsheboard_button)

    @allure.step
    def click_on_coupon_button(self):
        self._click(self.coupon_button)

    @allure.step
    def click_on_order_button(self):
        self._click(self.order_button)

    @allure.step
    def click_on_product_button(self):
        self._click(self.product_button)

    @allure.step
    def click_on_invoice_button(self):
        self._click(self.invoice_button)

    @allure.step
    def click_on_shping_button(self):
        self._click(self.shping_certificate_button)

    @allure.step
    def click_on_delivery_button(self):
        self._click(self.delivery_dasheboard)

    @allure.step
    def click_on_delivery(self):
        self._click(self.delevery_table)

    @allure.step
    def click_on_acskquestion_overview(self):
        self._click(self. acskquestion_overview)

    @allure.step
    def verify_the_title_of_the_page(self):
        return self._find(self.dasheboard_text).text

    @allure.step
    def displaying(self, display):
        return self._is_displayed(display)

    @allure.step
    def click_on_dasheboard_finance(self):
        self._click(self.title_with_finance)

    @allure.step
    def color(self, location):
        element_color = self._find(location).value_of_css_property("background-color")
        return element_color

    @allure.step
    def checking_font_size(self, location):
        return self._find(location).value_of_css_property("font-size")

    @allure.step
    def checking_font_weidth(self, location):
        return self._find(location).value_of_css_property("font-weidth")

    @allure.step
    def checking_text_align(self, location):
        return self._find(location).value_of_css_property("text-align")





