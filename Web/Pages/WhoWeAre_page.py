
import allure

from Web.Data.data2 import Data2
from Web.Locators.Locators_who_we_are import Locators_who_we_are
from Web.Pages.utilities import Utilities


class WhoWeArePage(Utilities, Locators_who_we_are, Data2):

    @allure.step
    @allure.description("select option one")
    def select_the_options_1(self):
        self._click(self.option1)

    @allure.step
    @allure.description("select option two")
    def select_the_options_2(self):
        self._click(self.option2)

    @allure.step
    @allure.description("click on save button")
    def save_btn(self):
        self._click(self.save)


    @allure.step
    @allure.description("scroll dawn to the footer")
    def scroll_dawn(self):
        self.scroll(self.footer, 1000)
        text = self._find(self.pratim_text1).text
        assert text in ""

    @allure.step
    @allure.description("click on who we are link text")
    def click_who_we_are_link_text(self):
        self._click(self.path_who_we_are)
        # text = self._find(self.path_who_we_are).text
        # assert text in "הזירה שמפגישה בין ספקים לקמעונאים"

    @allure.step
    @allure.description("click on lezirat hamishar button")
    def click_lezirat_hamishar_btn(self):
        self._click(self.mischar_button)
        text = self._find(self.welcome_text).text
        assert text in "ברוכים הבאים ל-"

    @allure.step
    @allure.description("click on peratim nosafim button")
    def click_pratim_nosafim_btn(self):
        self._click(self.pratim_nosafim_button)
        self.scroll(self.pratim_text1, 300)
        text1 = self._find(self.pratim_text1).text
        assert text1 in "אז איך זה עובד?"
        text2 = self._find(self.pratim_text2).text
        assert text2 in "מוצר חדש עולה לזירה"
        text3 = self._find(self.pratim_text3).text
        assert text3 in "משלוח מהיר מדלת לדלת"

    @allure.step
    @allure.description("click on create contact button")
    def click_create_contact_btn(self):
        self._click(self.create_contact_button)
        text1 = self._find(self.create_contact_text1 ).text
        assert text1 in "נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה."
        text2 = self._find(self.create_contact_text2).text
        assert text2 in "שירות לקוחות"

    @allure.step
    @allure.description("click on new order button")
    def click_new_order_btn(self):
        self._click(self.new_order_button)
        text1 = self._find(self.welcome_text).text
        assert text1 in "ברוכים הבאים ל-"

    @allure.step
    @allure.description("check 'מערך משלוחים טכנולוגי' description found on who we are page")
    def check_maarah_mishlohim_description(self):
        text = self._find(self.maarah_mishlohim_text).text
        assert text in "מערך משלוחים טכנולוגי"

    @allure.step
    @allure.description("check 'אפשרויות תשלום מתקדמות' description found on who we are page")
    def check_efshariyot_tashlum_description(self):
        text = self._find(self.efshariyot_tashlum_text).text
        assert text in "אפשרויות תשלום מתקדמות"

    @allure.step
    @allure.description("check 'רכישה ומכירה אנונימית' description found on who we are page")
    def check_rekisha_ve_mehira_description(self):
        text = self._find(self.rkisha_ve_mehira_text).text
        assert text in "רכישה ומכירה אנונימית"