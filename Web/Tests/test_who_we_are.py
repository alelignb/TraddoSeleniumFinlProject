
from Web.Pages.WhoWeAre_page import *


class Test(WhoWeArePage):

    @allure.description("Verify who we are link text functionality")
    def test_who_we_are_link_text(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()

    @allure.description("verify 'לזירת המסחר' buuton functionality found on who we are page")
    def test_lezirat_ha_mishar_btn(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()
        self.switching_window()
        self.click_lezirat_hamishar_btn()

    @allure.description("verify  'פרתים נוספים' buuton functionality found on who we are page")
    def test_pratim_nosafim_btn(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()
        self.switching_window()
        self.click_pratim_nosafim_btn()

    @allure.description("verify new order button functionality found on who we are page")
    def test_hazmana_hadasha_btn(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()
        self.switching_window()
        self.click_new_order_btn()

    @allure.description("verify create contact button functionality found on who we are page")
    def test_tsur_kesher_btn(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()
        self.switching_window()
        self.click_create_contact_btn()

    @allure.description("check 'רכישה ומכירה אנונימית' description found on who we are page")
    def test_checking_rekisha_ve_mehira_description(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()
        self.switching_window()
        self.check_rekisha_ve_mehira_description()

    @allure.description("check 'אפשרויות תשלום מתקדמות' description found on who we are page")
    def test_checking_efshariyot_tashlum_description(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()
        self.switching_window()
        self.check_efshariyot_tashlum_description()

    @allure.description("check 'מערך משלוחים טכנולוגי' description found on who we are page")
    def test_checking_maarah_mishlohim_description(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()
        self.switching_window()
        self.check_maarah_mishlohim_description()

    @allure.description("check texts and descriptions founds on who we are page")
    def test_checking_all_description(self):
        self.open()
        self.select_the_options_1()
        self.select_the_options_2()
        self.save_btn()
        self.click_who_we_are_link_text()
        self.switching_window()
        self.check_maarah_mishlohim_description()
        self.check_efshariyot_tashlum_description()
        self.check_rekisha_ve_mehira_description()
