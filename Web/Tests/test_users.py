
import time
from Web.Pages.Users_Page import *


class Test(UsersPage):

    @allure.description("Verify admin login")
    def test_login_to_admin(self):
        self.open_admin()
        self.insert_login_phone_no()
        self.send_me_code_button()
        time.sleep(2)
        self.insert_login_password()
        self.login_button()

    @allure.description("Verify users category clickable")
    def test_users_clickable(self):
        # self.test_login_to_admin()
        self.open_admin()
        self.insert_login_phone_no()
        self.send_me_code_button()
        time.sleep(2)
        self.insert_login_password()
        self.login_button()
        self.click_users_category()

    @allure.description("Verify search existing user")
    def test_search_existing_user(self):
        self.open_admin()
        self.insert_login_phone_no()
        self.send_me_code_button()
        time.sleep(2)
        self.insert_login_password()
        self.login_button()
        self.click_users_category()
        self.search_users(self.name)
        text = self._find(self.user_first_data).text
        assert text in "mesganaw"

    @allure.description("Verify search non existing user")
    def test_search_non_existing_user(self):
        self.test_users_clickable()
        self.search_users("+++++++hfg")

    @allure.description("Verify display 75 option works correctly")
    def test_display_75(self):
        self.test_users_clickable()
        self.click_on_number_display_btn()
        self.click_on_number_display_options(self.display_75)

    @allure.description("Verify display 20 option works correctly")
    def test_display_20(self):
        self.test_users_clickable()
        self.click_on_number_display_btn()
        self.click_on_number_display_options(self.display_20)

    @allure.description("Verify display 50 option works correctly")
    def test_display_50(self):
        self.test_users_clickable()
        self.click_on_number_display_btn()
        self.click_on_number_display_options(self.display_50)
        text = self._find(self.display_text).text
        assert "מציג 1-50 מתוך 428 שורות" in text

    @allure.description("Verify display 100 option works correctly")
    def test_display_100(self):
        self.test_users_clickable()
        self.click_on_number_display_btn()
        self.click_on_number_display_options(self.display_100)

    @allure.description("Verify display 150 option works correctly")
    def test_display_150(self):
        self.test_users_clickable()
        self.click_on_number_display_btn()
        self.click_on_number_display_options(self.display_150)

    @allure.description("Verify display 200 option works correctly")
    def test_display_200(self):
        self.test_users_clickable()
        self.click_on_number_display_btn()
        self.click_on_number_display_options(self.display_200)

    @allure.description("Verify display all option works correctly")
    def test_display_all(self):
        self.test_users_clickable()
        self.click_on_number_display_btn()
        self.click_on_number_display_options(self.display_all)

    @allure.description("Verify on users category user settings works")
    def test_user_settings(self):
        self.test_users_clickable()
        self.click_users_settings()
        assertion = self._find(self.add_by_brand).text
        assert "add by brand" in assertion
        assertion = self._find(self.yevuwa).text
        assert "ייבוא" in assertion

    @allure.description("Verify if yetsuwa category functionality")
    def test_yetsuwa(self):
        self.test_users_clickable()
        self.click_users_settings()
        self.click_on_user_setting_categories(self.yetsuwa)

    @allure.description("Verify if yevuwa category functionality")
    def test_yevuwa(self):
        self.test_users_clickable()
        self.click_users_settings()
        self.click_on_user_setting_categories(self.yevuwa)

    @allure.description("Verify if add by brand category functionality/ works correctly")
    def test_add_by_brand(self):
        self.test_users_clickable()
        self.click_users_settings()
        self.click_on_user_setting_categories(self.add_by_brand)
        assertion = self._find(self.add_by_brand_text).text
        assert "מותג" in assertion

    @allure.description("Verify if structure category functionality")
    def test_structure(self):
        self.test_users_clickable()
        self.click_users_settings()
        self.click_on_user_setting_categories(self.structure)

    @allure.description("Verify if addition category functionality")
    def test_addition(self):
        self.test_users_clickable()
        self.click_users_settings()
        self.click_on_user_setting_categories(self.add_user)
        assertion = self._find(self.users_text).text
        assert assertion in "משתמשים"

    @allure.description("Verify if single arrow forward show next page works")
    def test_addition(self):
        self.test_users_clickable()
        self.click_on_arrows(self.single_arrow)
        assertion = self._find(self.single_number_before_txt).text
        assert "1" in assertion

    @allure.description("Verify if double arrow shows the last page works")
    def test_addition(self):
        self.test_users_clickable()
        self.click_on_arrows(self.double_arrow)
        assertion = self._find(self.double_num_before_txt).text
        assert "8" in assertion

    @allure.description("Verify if click on forward change page numbers show next page works")
    def test_forward_number(self):
        self.test_users_clickable()
        self.click_on_arrows(self.number_change_forward)
        assertion = self._find(self.second_num_txt).text
        assert "3" in assertion

    @allure.description("Verify if click on backward change page numbers show previous page works")
    def test_backward_number(self):
        self.test_users_clickable()
        self.click_on_arrows(self.number_change_backward)
        assertion = self._find(self.number_change_forward).text
        assert "2" in assertion

    @allure.description("Verify if change to english icon works")
    def test_english_icon(self):
        self.test_users_clickable()
        self.click_language_icons(self.english_icon)
        time.sleep(2)
        assertion = self._find(self.user_txt_english).text
        assert "Users" in assertion

    @allure.description("Verify if change to hebrew icon works after we change to english language")
    def test_hebrew_icon(self):
        self.test_users_clickable()
        self.click_language_icons(self.english_icon)
        time.sleep(2)
        self.click_language_icons(self.hebrew_icon)
        time.sleep(2)
        assertion = self._find(self.users_text).text
        assert "משתמשים" in assertion


















