import allure
from Web.Data.data import *
import pytest
from Web.Pages.ddt_page import DdtPage


class Test_DataDriveForRegistration(DdtPage):
    def handle_the_first_popup(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if register works with different data")
    @pytest.mark.parametrize("phone, id_no, fname, lname, email, town, home", [test1, test2, test3])
    def test_ddt_register_with_valid_user_data(self, phone, id_no, fname, lname, email, town, home):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_ddt_phone(phone)
        self.enter_ddt_id(self.id_field, id_no)
        self.click_checkbox()
        self.click_connection()
        assert self.checking_the_title(self.page_title2) == 'רק מוודאים שאנחנו מכירים'
        self.enter_code_ddt(self.login_code(f'{phone}'))
        self.press_perform_verification_button()
        self._is_displayed(self.etrado_title)
        self.select_food()
        self.select_drink()
        self.crate_account_button()
        self.edit_button()
        self.enter_name_ddt(self.fn, fname)
        self.enter_name_ddt(self.ln, lname)
        self.enter_email_ddt(email)
        self.enter_ddt_id(self.tz, id_no)
        self.enter_city_ddt(town)
        self.enter_street_ddt(home)
        self.saving_button()
        self._driver.close()


