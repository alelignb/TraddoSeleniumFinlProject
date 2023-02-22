
import allure

from Web.Data.data import Data
from Web.Locators.Locators_canabis import Locators_Cannabis
from Web.Pages.utilities import Utilities


class CannabisPage(Utilities, Locators_Cannabis, Data):

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
    @allure.description("click on cannabis link text")
    def click_cannabis_link_text(self):
        self._click(self.CANNABIS_URL)
        text = self._find(self.CANNABIS_TEXT).text
        assert text in "קנאביס"

    @allure.step
    @allure.description("Check cart found on cannabis page")
    def check_cart(self,):
        text = self._find(self.CART_URL).text
        assert text in "סל הקניות שלך"
        assert text in "העגלה שלך ריקה"

    @allure.step
    @allure.description("Click on one product on cannabis page")
    def click_product(self, ):
        self._click(self.product)
        text = self._find(self.product_text).text
        assert text in "שמן למון קוש"

    @allure.step
    @allure.description("Click on plus button")
    def click_plus_button(self, ):
        self._click(self.plus_button)
        text = self._find(self.product_text_on_cart).text
        assert text in "שמן למון קוש"

    @allure.step
    @allure.description("Click on minus button")
    def click_minus_button(self, ):
        self._click(self.minus_button)
        text = self._find(self.product_text_on_cart).text
        assert text in "שמן למון קוש"

    @allure.step
    @allure.description("Check max asakim found on cart page")
    def check_max_asakim(self, ):
        text = self._find(self.max_asakim).text
        assert text in "בזכות שיתוף הפעולה עם מקס, אין יותר סיבה לדאגה לתשלומים! סופיות עסקה, תשלום באופן ישיר בטוח לשימוש"

    @allure.step
    @allure.description("Check shelot nosafot description found on cannabis page")
    def check_shelot_nosafot(self, ):
        text = self._find(self.shelot_nosafot).text
        assert text in "שאלות נפוצות"
        text2 = self._find(self.shelot_nosafot2).text
        assert text2 in "איך עובד התשלום?"

    @allure.step
    @allure.description("Check yetsirat kesher description found on cannabis page")
    def check_yetsirat_kesher(self,):
        text = self._find(self.yetsirat_kesher).text
        assert text in "יצירת קשר"
        text2 = self._find(self.yetsirat_kesher2).text
        assert text2 in "לכל שאלה ובעיה אנחנו תמיד כאן,"

    @allure.step
    @allure.description("Check eah oved hashiluwah description found on cannabis page")
    def check_eah_oved_hashiluwah(self,):
        text = self._find(self.eah_oved_hashiluwah).text
        assert text in "איך עובד השילוח"
        text2 = self._find(self.eah_oved_hashiluwah2).text
        assert text2 in "שיטת השילוח שלנו נורא פשוטה."

    @allure.step
    @allure.description("scroll dawn to the footer")
    def scroll_dawn(self, locate):
        self.scroll(locate, 200)


    @allure.step
    @allure.description("Click on change to english icon")
    def click_english_icon(self,):
        self._click(self.english_icon)
        text = self._find(self.english_text).text
        assert text in "Cannabis"

    @allure.step
    @allure.description("Click on change to hebrew icon")
    def click_hebrew_icon(self, ):
        self._click(self.hebrew_icon)
        text = self._find(self.hebrew_text).text
        assert text in "קנאביס"

    @allure.step
    @allure.description("Click on whatsapp icon")
    def click_whatsapp_icon(self,):
        self._click(self.whatsapp)
        text = self._find(self.whatsapp_text).text
        assert text in "Trado Support"

    @allure.step
    @allure.description("Click on whatsapp send button")
    def click_send_button(self,):
        self._click(self.whatsapp_send_button)
        # text = self.find(self.english_text).text
        # assert text in "שמן למון קוש"

    @allure.step
    @allure.description("insert or type message on whatsapp")
    def type_whatsapp_message(self,):
        self._find(self.whatsapp_message).send_keys(self.whatsapp_message_text)

    @allure.step
    @allure.description("click on select chosen arrow price, from highest option")
    def option_from_highest(self, ):
        self._click(self.arrow_from_highest)

    @allure.step
    @allure.description("click on select chosen arrow price, from lowest option")
    def option_from_lowest(self, ):
        self._click(self.arrow_from_list)

    @allure.step
    @allure.description("click on select chosen arrow popularity option")
    def option_popularity(self, ):
        self._click(self.popularity)

    @allure.step
    @allure.description("click select options curser")
    def click_option_list(self, ):
        self._click(self.option_list)

    @allure.step
    @allure.description("click on list products diagonally button")
    def click_diagonal_button(self, ):
        self._click(self.order_diagonally_btn)

    @allure.step
    @allure.description("click on list products vertically button")
    def click_vertical_button(self, ):
        self._click(self.order_vertically_btn)

