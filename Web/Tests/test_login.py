
import allure
from Web.Pages.login_page import LoginPage


class Test_Login(LoginPage):

    def handle_the_first_popup(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify if the page title of the login frame is correct")
    def test_the_page_title(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        assert self.checking_the_title(self.loginpage_title) == 'ברוכים השבים! מתרגשים לראות אתכם כאן'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the text weight of the login frame")
    def test_text_weight_page_title(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        assert self.checking_font_weight(self.loginpage_title) == '600'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the title of phone field")
    def test_title_of_phone_filed(self):
        self.handle_the_first_popup()
        self.click_save_button()
        self.click_myaccount_link()
        assert self.check_the_text(self.phone_field_text) == '*מס׳ הטלפון שלך'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the title of check box is correct")
    def test_title_of_check_box(self):
        self.handle_the_first_popup()
        self.click_save_button()
        self.click_myaccount_link()
        assert self.check_the_text(self.check_box_text) == 'זכור אותי לפעם הבאה'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the the color of connection button")
    def test_connection_button_color(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        assert self.color(self.connection_button) == 'rgba(255, 255, 255, 1)'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the the color of connect button")
    def test_connect_button_color(self):
        self.handle_the_first_popup()
        self.click_save_button()
        self.click_myaccount_link()
        assert self.color(self.connect_button) == 'rgba(47, 150, 185, 1)'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the background color of login frame is white")
    def test_background_color_of_th_page(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        assert self.color(self.page) == 'rgba(255, 255, 255, 1)'
        self._driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify if login works by entering all valid test datas")
    def test_login_correctly(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.enter_phone()
        self.click_connection()
        self.enter_login_code()
        self.press_login_button()
        self._is_displayed(self.etrado_title)
        self._driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify if login doesn't work without entering phone number")
    def test_login_without_phone(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.click_connection()
        self.click_on_page()
        assert self.check_the_text(self.enter_phone_error) == 'נא למלא שדה זה'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if login doesn't work by entering invalid phone number")
    def test_login_with_invalid_phone(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self.enter_invalid_phone()
        self.click_connection()
        assert self.check_the_text(self.no_such_phone) == 'No Such User Please Register'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of twitter link")
    def test_twitter_link_functionality(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self._click(self.twitter_link)
        self.switching_window()
        assert self.checking_current_url() != self.url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of google link")
    def test_google_link_functionality(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self._click(self.google_link)
        self.switching_window()
        assert self.checking_current_url() != self.url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of facebook link")
    def test_facebook_link_functionality(self):
        self.handle_the_first_popup()
        self.click_myaccount_link()
        self._click(self.facebook_link)
        assert self.checking_current_url() != self.url
        self._driver.close()
