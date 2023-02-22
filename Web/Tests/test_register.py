import time
import allure
from Web.Pages.register_page import RegisterPage


class Test_Register(RegisterPage):

    def handle_the_first_popup(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify if the color of the register button is correct")
    def test_color_register_button(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        assert self.color(self.register_button) == 'rgba(47, 150, 185, 0.22)'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Check ift the title of register page is correct")
    def test_the_title_of_register_page(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        time.sleep(2)
        assert self.checking_the_title(self.register_title) == 'כיף שבאתם! כבר יוצרים לכם מקום בזירה'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Check if the title of phone field is correct")
    def test_text_above_phone_field(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        time.sleep(2)
        assert self.checking_the_title(self.phone_field_text) == '*מס׳ הטלפון שלך'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Check the title of id_field is correct")
    def test_text_above_id_field(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        time.sleep(2)
        assert self.checking_the_title(self.id_no_text) == '*מס׳ הטלפון שלך'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the title of check box is correct")
    def test_text_for_security_check_box(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        time.sleep(2)
        assert self.checking_the_title(self.check_box_text) == 'קראתי ואני מאשר/ת את תקנון השימוש ומדיניות הפרטיות'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if register doesn't work without user data")
    def test_register_without_user_data(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.click_connection()
        self.click_on_page()
        assert self.check_the_text(self.empty_phone_error) == 'נא למלא שדה זה'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if register doesn't work without phone")
    def test_register_without_phone(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_id_number()
        self.click_connection()
        self.click_on_page()
        assert self.check_the_text(self.empty_phone_error) == 'נא למלא שדה זה'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if register doesn't work without id")
    def test_register_without_id(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_new_phone()
        self.click_checkbox()
        self.click_connection()
        self.click_on_page()
        assert self.check_the_text(self.empty_id_error) == ('Cast To String Failed For Value "{ Error: \'Business '
                                                            'Number Is Required\' }" At Path "OfId"')
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if register is not working with invalid phone")
    def test_register_with_invalid_phone(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_invalid_phone()
        self.enter_id_number()
        self.click_checkbox()
        self.click_connection()
        self.click_on_page()
        assert self.check_the_text(self.invalid_phone_error) == 'מס׳ טלפון לא תקין'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if register is not working with invalid id")
    def test_register_with_invalid_id(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_new_phone()
        self.enter_id_number()
        self.click_checkbox()
        self.click_connection()
        assert self.checking_the_title(self.page_title2) != 'רק מוודאים שאנחנו מכירים'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if register is not working with all invalid data")
    def test_register_with_invalid_user_data(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_invalid_phone()
        self.enter_id_number()
        self.click_checkbox()
        self.click_connection()
        assert self.checking_the_title(self.page_title2) != 'רק מוודאים שאנחנו מכירים'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Check if register doesn't work with existing phone")
    def test_register_with_existing_phone(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_existing_phone()
        self.enter_id_number()
        self.click_checkbox()
        self.click_connection()
        assert self.check_the_text(self.existing_phone_error) == 'שדה צריך להיות ייחודיי'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if register is working with all valid data")
    def test_register_with_valid_user_data(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_new_phone()
        self.enter_id_number()
        self.click_checkbox()
        self.click_connection()
        assert self.checking_the_title(self.page_title2) == 'רק מוודאים שאנחנו מכירים'
        self.enter_register_code()
        self.press_perform_verification_button()
        self._is_displayed(self.etrado_title)
        self.select_food()
        self.select_drink()
        self.crate_account_button()
        self.edit_button()
        self.enter_name(self.fn, self.firstname)
        self.enter_name(self.ln, self.lastname)
        self.enter_email(self.em, self.email_address)
        self.enter_id(self.tz, self.valid_id)
        self.enter_city(self.irr, self.town)
        self.enter_street(self.mispar, self.home_num)
        self.saving_button()
        time.sleep(3)
        assert self.check_on_server()['firstName'] == self.firstname
        assert self.check_on_server()['lastName'] == self.lastname
        assert self.check_on_server()['email'] == self.email_address
        self._driver.close()

