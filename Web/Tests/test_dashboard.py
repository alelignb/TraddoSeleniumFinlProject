import time
import allure
from Web.BasePage.basepage import BasePage
from Web.Pages.dashboard_page import dashboard_page


class TestDashboard(dashboard_page, BasePage):
    def handling_the_first_popup(self):
        self.open_admin()
        self.fill_values_to_phone_correct(self.valid_phone)
        self._click(self.phone_code)
        time.sleep(5)
        self.fill_values_to_passward_field(self.valid_passward)
        self._click(self.check_box)
        self._click(self.connection_button)

    @allure.description("Verify if we can send  with  all valid data")
    def test_first_correct_page(self):
        self.open_admin()
        self.fill_values_to_phone_correct(self.valid_phone)
        self._click(self.phone_code)
        time.sleep(5)
        self.fill_values_to_passward_field(self.valid_passward)
        self._click(self.check_box)
        self._click(self.connection_button)

    @allure.description("Verify the of dasheboard is Clickable")
    def test_dasheboard_buttons(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()

    @allure.description("test the of Coupon button is Clickable")
    def test_couponn_button(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_coupon_button()

    @allure.description("test the of order button is Clickable")
    def test_order_button(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_order_button()

    @allure.description("test the of product button is Clickable")
    def test_product_button(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_product_button()

    @allure.description("test the of invoice button is Clickable")
    def test_invoice_button(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_invoice_button()

    @allure.description("test the of product shping is Clickable")
    def test_ceritificate_button(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_shping_button()

    @allure.description("test the of delivery button is Clickable")
    def test_delivery_button(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_delivery_button()

    @allure.description("test the of delivery section ")
    def test_delivery(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_delivery()

    @allure.description("test the of acskquestion overview is Clickable")
    def test_acskquestion_overview(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_acskquestion_overview()

    @allure.description("test the of acskquestion overview is Clickable")
    def test_text_dasheboard_title(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        assert self.verify_the_title_of_the_page() == 'דשבורד'
        self._driver.close()

    @allure.description("test the of acskquestion overview is Clickable")
    def test_finance_title(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        self.click_on_dasheboard_finance()
        self._driver.close()

    @allure.description("Verifying font size of the label to dasheboard text font is displayed")
    def test_dasheboard_text_font_size(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        assert self.checking_font_size(self.dashboard_page_font) == '16px'

    @allure.description("Verifying font width of the label to dashboard ")
    def test_label_on_dasheboarde_font_width(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        assert self.checking_font_weidth(self.dasheboard_page_width) == ''

    @allure.description("Verifying   of the dasheboard page graph is  displayed ")
    def test_dasheboard_page_graph(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        assert self.color(self.dashboard_page_graph) == 'rgba(0, 0, 0, 0)'

    @allure.description("Verifying back_ground color of the dasheboard page displayed")
    def test_verifying_dasheboard_page_color(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        assert self.color(self.dasheboard_all_pages) == 'rgba(0, 0, 0, 0)'

    @allure.description("Verifying if the dasheboard form is displayed")
    def test_verifying_dasheboard_page_form_displaying(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        assert self.displaying(self.dsheboard_footer) == True

    @allure.description("Verifying if there are graph on the dasheboarde is clicable ")
    def test_verifying_dasheboard_page_graph_on_right_side(self):
        self.handling_the_first_popup()
        self.click_on_dsheboard_button()
        assert self.displaying(self.dashboard_page_graph) == True
