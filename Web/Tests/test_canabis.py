import pytest
from Web.Pages.Canabis_page import *


class Test(CannabisPage):

    @allure.description("Verify cannabis link text functionality")
    def test_cannabis_link_text(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self._driver.close()

    @allure.description("Verify trado interface with whatsapp")
    def test_whatsapp_interface(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_whatsapp_icon()
        self._driver.close()

    @allure.description("Test send message on whatsapp")
    def test_send_whatsapp_message(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_whatsapp_icon()
        self.type_whatsapp_message()
        self.click_send_button()
        self._driver.close()

    @allure.description("Test/ verify change to english language icon works correctly")
    def test_english_icon(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_english_icon()
        self._driver.close()

    @allure.description("Test/ verify change back to hebrew language icon works "
                        "correctly after we change language in english")
    def test_hebrew_icon(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_english_icon()
        self.click_hebrew_icon()
        self._driver.close()

    @allure.description("Test/ verify products clickable")
    def test_products_clickable(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_product()
        self._driver.close()

    @allure.description("Test/ verify plus products to cart")
    @pytest.mark.sanity
    def test_plus_products_to_cart(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_product()
        self.click_plus_button()
        self._driver.close()

    @allure.description("Test/ verify minus or delete products to cart")
    def test_minus_delete_products_to_cart(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_product()
        self.click_plus_button()
        self.click_minus_button()
        self._driver.close()

    @allure.description("verify if list products vertically button works correctly")
    def test_order_products_vertically(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_vertical_button()
        self._driver.close()

    @allure.description("verify if list products diagonally button works correctly after we change vertically")
    def test_order_products_diagonally(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_vertical_button()
        self.click_diagonal_button()
        self._driver.close()

    @allure.description("verify if select chosen arrow price, from lowest works correctly")
    def test_option_from_lowest(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_option_list()
        self.option_from_lowest()
        self._driver.close()

    @allure.description("verify if select chosen arrow price, from highest works correctly")
    def test_option_from_highest(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_option_list()
        self.option_from_highest()
        self._driver.close()

    @allure.description("verify if select chosen arrow popularity works correctly")
    def test_option_from_lowest(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.click_option_list()
        self.option_from_lowest()
        self.option_popularity()
        self._driver.close()

    @allure.description("check common questions found on cannabis page")
    def test_checking_shelot_nosafot(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.check_shelot_nosafot()
        self._driver.close()

    @allure.description("check contact found on cannabis page")
    def test_checking_yetsirat_kesher(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.check_yetsirat_kesher()
        self._driver.close()

    @allure.description("check how shipment works description found on cannabis page")
    def test_checking_eah_oved_hashiluwah(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.check_eah_oved_hashiluwah()
        self._driver.close()

    @allure.description("check MAX עסקים description found on cannabis page")
    def test_checking_MAX_asakim(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.check_max_asakim()
        self._driver.close()

    @allure.description("check texts and descriptions founds on cannabis page")
    def test_checking_all_descriptions(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_cannabis_link_text()
        self.check_max_asakim()
        self.check_eah_oved_hashiluwah()
        self.check_yetsirat_kesher()
        self.check_shelot_nosafot()
        self._driver.close()

