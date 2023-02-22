import allure

from Web.Pages.e2e_page import E2ePage


class Test_E2e(E2ePage):

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("verify all process of purchasing product using phone payment system")
    def test_e2e_phone_patment(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_new_phone()
        self.enter_id_number()
        self.click_checkbox()
        self.click_connection()
        assert self.checking_the_title(self.page_title2) == 'רק מוודאים שאנחנו מכירים'
        self.enter_register_code()
        self.press_perform_verification_button()
        self.select_food()
        self.select_drink()
        self.crate_account_button()
        self._is_displayed(self.etrado_title)
        self.edit_button()
        self.enter_name(self.fn, self.firstname)
        self.enter_name(self.ln, self.lastname)
        self.enter_email(self.em, self.email_address)
        self.enter_id(self.tz, self.my_id)
        self.enter_city(self.irr, self.town)
        self.enter_street(self.mispar, self.street_name)
        self.saving_button()
        self.previous_page()
        self.click_the_product(self.og_kush)
        self.click_plus_icon()
        self.press_checkout_button()
        self.enter_name(self.business_name, self.random_name())
        self.enter_id(self.id_num, self.my_id)
        self.enter_email(self.business_email, self.email_address)
        self.enter_city(self.city, self.town)
        self.enter_street(self.street, self.street_name)
        self.enter_home(self.home, self.home_num)
        self.enter_get(self.entrance, self.enter)
        self.enter_floor(self.floor, self.floor_num)
        self.enter_name(self.business_name2, self.random_name())
        self.enter_name(self.fst_name, self.firstname)
        self.enter_name(self.lst_name, self.lastname)
        self.click_finish_button()
        self.select_payment(self.payment_option)
        self.enter_branch(self.branch_num)
        self.enter_card_num_e2e(self.card_number)
        self.click_confirm()
        self.click_pay()
        self.back()
        assert self.check_on_server()['email'] == self.email_address
        assert self.check_on_server()['firstName'] == self.firstname
        assert self.check_on_server()['address']['city'] == self.town
        assert self.check_on_server()['address']['street'] == self.street_name
        self._driver.close()


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("verify all process of purchasing product using phone payment system")
    def test_e2e_with_credit_card(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_myaccount_link()
        self.click_register_button()
        self.enter_new_phone()
        self.enter_id_number()
        self.click_checkbox()
        self.click_connection()
        assert self.checking_the_title(self.page_title2) == 'רק מוודאים שאנחנו מכירים'
        self.enter_register_code()
        self.press_perform_verification_button()
        self.select_food()
        self.select_drink()
        self.crate_account_button()
        self._is_displayed(self.etrado_title)
        self.edit_button()
        self.enter_name(self.fn, self.firstname)
        self.enter_name(self.ln, self.lastname)
        self.enter_email(self.em, self.email_address)
        self.enter_id(self.tz, self.my_id)
        self.enter_city(self.irr, self.town)
        self.enter_street(self.mispar, self.street_name)
        self.saving_button()
        self.previous_page()
        self.click_the_product(self.og_kush)
        self.click_plus_icon()
        self.press_checkout_button()
        self.enter_name(self.business_name, self.random_name())
        self.enter_id(self.id_num, self.my_id)
        self.enter_email(self.business_email, self.email_address)
        self.enter_city(self.city, self.town)
        self.enter_street(self.street, self.street_name)
        self.enter_home(self.home, self.home_num)
        self.enter_get(self.entrance, self.enter)
        self.enter_floor(self.floor, self.floor_num)
        self.enter_name(self.business_name2, self.random_name())
        self.enter_name(self.fst_name, self.firstname)
        self.enter_name(self.lst_name, self.lastname)
        self.click_finish_button()
        self.select_payment(self.new_card)
        self.switching_to_iframe()
        self.enter_card_num(self.card_number)
        self.enter_id_for_card(self.payment_id)
        self.select_exp_date(self.expyear, self.card_year)
        self.select_exp_date(self.expmon, self.card_mon)
        self.enter_credit_card(self.cvv, self.card_cvv)
        self.press_credit_pay_button()
        assert self.check_on_server()['email'] == self.email_address
        assert self.check_on_server()['firstName'] == self.firstname
        assert self.check_on_server()['address']['city'] == self.town
        assert self.check_on_server()['address']['street'] == self.street_name
        self._driver.close()





